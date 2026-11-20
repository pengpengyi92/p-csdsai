import { describe, expect, it } from 'vitest';
import { GitHubReader, LIMITS, parseRepository } from '../src/core/github';

const ref = parseRepository('https://github.com/example/fixture');
const sha = 'a'.repeat(40);

describe('GitHub schema compatibility after dependency patches', () => {
  it('accepts public metadata and a pinned commit, stripping unknown fields', async () => {
    let calls = 0;
    const reader = new GitHubReader(async () => Response.json(++calls === 1
      ? { private: false, default_branch: 'main', description: null, extra: 'ignored' }
      : { sha, commit: { tree: { sha } }, extra: 'ignored' }));
    await expect(reader.metadata(ref)).resolves.toEqual({ commit: sha, tree: sha, description: '' });
    expect(calls).toBe(2);
  });

  it.each([
    { private: 'false', default_branch: 'main', description: '' },
    { private: false, description: '' },
    { private: false, default_branch: 'main', description: 1 },
  ])('rejects malformed metadata without reading a commit: %j', async (metadata) => {
    let calls = 0;
    const reader = new GitHubReader(async () => {
      calls++;
      return Response.json(metadata);
    });
    await expect(reader.metadata(ref)).rejects.toThrow();
    expect(calls).toBe(1);
  });

  it('rejects an unpinned commit response', async () => {
    let calls = 0;
    const reader = new GitHubReader(async () => Response.json(++calls === 1
      ? { private: false, default_branch: 'main', description: '' }
      : { sha: 'main', commit: { tree: { sha } } }));
    await expect(reader.metadata(ref)).rejects.toThrow();
    expect(calls).toBe(2);
  });

  it('rejects malformed tree entries', async () => {
    const reader = new GitHubReader(async () => Response.json({
      truncated: false,
      tree: [{ path: 'agent.ts', mode: '100644', type: 'blob', sha: 'invalid', size: 10 }],
    }));
    await expect(reader.tree(ref, sha)).rejects.toThrow();
  });

  it('rejects an oversized blob declaration before decoding content', async () => {
    const reader = new GitHubReader(async () => Response.json({
      encoding: 'base64', size: LIMITS.fileBytes + 1, content: 'not-base64',
    }));
    await expect(reader.blob(ref, {
      path: 'agent.ts', sha, size: 10, mode: '100644', type: 'blob',
    })).rejects.toThrow();
  });
});
