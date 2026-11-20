import { test, expect } from '@playwright/test';
import { readFile } from 'node:fs/promises';
import type { JobState, TrustReport } from '../../src/types';

test('archived report replay reloads and exports the pinned commit (no live scan)', async ({ page }, info) => {
  const body = await readFile('docs/reports/self-inspection-2026-09-09.json', 'utf8');
  const report = JSON.parse(body) as TrustReport;
  const errors: string[] = [];
  let requests = 0;
  page.on('pageerror', error => errors.push(error.message));
  // Replay a completed job and archived report; this does not verify live DO persistence.
  const job: JobState = {
    id: report.id, ref: report.repository.ref, stage: 'complete', status: 'completed',
    created_at: report.created_at, updated_at: report.created_at,
    expires_at: new Date(Date.parse(report.created_at) + 86_400_000).toISOString(),
    attempt: 1, error: null, progress: { done: 1, total: 1 }, history: [],
  };
  await page.route(`**/api/jobs/${report.id}`, route => route.fulfill({ json: job }));
  await page.route(`**/api/reports/${report.id}`, async route => {
    requests++;
    await route.fulfill({ contentType: 'application/json', body });
  });
  await page.goto(`/?report=${report.id}`);
  await expect(page.getByText('PUBLIC REPOSITORY SNAPSHOT', { exact: true })).toBeVisible();
  await expect(page.locator('.main-score strong')).toHaveText(String(report.overall_score));
  await page.reload();
  await expect(page.locator('.main-score strong')).toHaveText(String(report.overall_score));
  expect(requests).toBe(2);
  await page.getByRole('tab', { name: 'Coverage', exact: true }).click();
  await expect(page.getByRole('heading', { name: 'Skipped files' })).toBeVisible();
  const pending = page.waitForEvent('download');
  await page.getByRole('button', { name: 'Download Markdown' }).click();
  const download = await pending;
  expect(download.suggestedFilename()).toBe(`p-trust-${report.repository.ref.name}.md`);
  const path = await download.path();
  expect(path).not.toBeNull();
  const markdown = await readFile(path!, 'utf8');
  expect(markdown).toContain(`- Commit: ${report.repository.commit_sha}`);
  expect(markdown).toContain(`- Score: ${report.overall_score} / 100`);
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1)).toBe(true);
  expect(errors).toEqual([]);
  await page.screenshot({ path: `output/${info.project.name}-archived-replay.png`, fullPage: true });
});
