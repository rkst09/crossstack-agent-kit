import { describe, expect, it } from 'vitest';
import { formatEmployeeName, type Employee } from './employee';

describe('formatEmployeeName', () => {
  it('returns a safe fallback for a null display name', () => {
    const employee: Employee = {
      id: 1,
      displayName: null,
      department: 'Operations',
    };

    expect(formatEmployeeName(employee)).toBe('Unknown employee');
  });

  it('returns a safe fallback when the display name is missing', () => {
    const employee: Employee = {
      id: 1,
      department: 'Operations',
    };

    expect(formatEmployeeName(employee)).toBe('Unknown employee');
  });

  it('returns a safe fallback for a blank display name', () => {
    const employee: Employee = {
      id: 1,
      displayName: '  \t ',
      department: 'Operations',
    };

    expect(formatEmployeeName(employee)).toBe('Unknown employee');
  });

  it('formats a non-null display name', () => {
    const employee: Employee = {
      id: 2,
      displayName: 'Asha Rao',
      department: 'Engineering',
    };

    expect(formatEmployeeName(employee)).toBe('ASHA RAO');
  });
});
