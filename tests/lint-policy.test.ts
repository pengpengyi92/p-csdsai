import { ESLint } from 'eslint';
import { describe, expect, it } from 'vitest';

const filePath = 'src/dependency-policy.fixture.ts';

describe('retained TypeScript lint policy', () => {
  it('accepts a valid typed transformation under the actual repository config', async () => {
    const [result] = await new ESLint().lintText(
      'type Order = { quantity: number }; export function units(order: Order): number { return order.quantity; }',
      { filePath },
    );
    expect(result.messages).toEqual([]);
  });

  it('still rejects unused variables through the TypeScript rule', async () => {
    const [result] = await new ESLint().lintText(
      'export function units(quantity: number): number { const unused = 1; return quantity; }',
      { filePath },
    );
    expect(result.messages.map(message => message.ruleId)).toContain('@typescript-eslint/no-unused-vars');
    expect(result.errorCount).toBeGreaterThan(0);
  });

  it('still rejects explicit any rather than weakening checks to remove a dependency', async () => {
    const [result] = await new ESLint().lintText(
      'export function identity(value: any) { return value; }',
      { filePath },
    );
    expect(result.messages.map(message => message.ruleId)).toContain('@typescript-eslint/no-explicit-any');
    expect(result.errorCount).toBeGreaterThan(0);
  });
});
