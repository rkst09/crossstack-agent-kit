import { useEffect, useState } from 'react';
import { formatEmployeeName, type Employee } from './employee';

export function App() {
  const [employee, setEmployee] = useState<Employee | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let cancelled = false;

    async function loadEmployee() {
      try {
        const response = await fetch('/api/employees/1');
        if (!response.ok) {
          throw new Error(`Employee request failed with HTTP ${response.status}`);
        }

        // INTENTIONAL CONTRACT GAP: JSON is asserted to Employee without runtime validation.
        const data = (await response.json()) as Employee;
        if (!cancelled) setEmployee(data);
      } catch (cause) {
        if (!cancelled) {
          setError(cause instanceof Error ? cause.message : 'Unknown request error');
        }
      }
    }

    void loadEmployee();
    return () => {
      cancelled = true;
    };
  }, []);

  return (
    <main style={{ fontFamily: 'system-ui, sans-serif', margin: '3rem auto', maxWidth: 680, padding: '0 1rem' }}>
      <h1>CrossStack Contract Lab</h1>
      <p>This sample demonstrates safe handling of nullable API fields.</p>
      {error && <p role="alert">{error}</p>}
      {!error && !employee && <p>Loading employee…</p>}
      {employee && (
        <section aria-label="Employee details">
          <p><strong>Name:</strong> {formatEmployeeName(employee)}</p>
          <p><strong>Department:</strong> {employee.department}</p>
        </section>
      )}
    </main>
  );
}
