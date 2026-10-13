export type Employee = {
  id: number;
  displayName?: string | null;
  department: string;
};

export function formatEmployeeName(employee: Employee): string {
  const displayName = employee.displayName;
  return displayName?.trim() ? displayName.toUpperCase() : 'Unknown employee';
}
