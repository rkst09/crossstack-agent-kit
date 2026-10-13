# Cross-Stack Contract Lab

A small, **working** example that demonstrates how a nullable field returned by ASP.NET Core is represented and handled by a React/TypeScript frontend.

It uses synthetic in-memory employee data. It makes no external API calls and does not connect to SharePoint or a Power Platform tenant.

## Requirements

- .NET 10 SDK
- Node.js 22.12 or later recommended for the Vite 7 toolchain, and npm

## Start the API

From the repository root:

```powershell
dotnet run --project examples/cross-stack-contract-lab/backend/EmployeeApi
```

The API listens on `http://127.0.0.1:5080` by launch settings.

Inspect the nullable response:

```powershell
Invoke-RestMethod http://127.0.0.1:5080/api/employees/1 | ConvertTo-Json
```

Expected response:

```json
{
  "id": 1,
  "displayName": null,
  "department": "Operations"
}
```

Employee 2 has a normal display name. Unknown IDs return HTTP 404. The API contract intentionally allows a nullable display name.

## Verify the frontend

Open a second terminal:

```powershell
cd examples/cross-stack-contract-lab/frontend
npm install
npm run typecheck
npm test
npm run build
```

Expected behavior:

- type checking passes;
- four unit tests pass (null, missing, blank, and normal names);
- production build succeeds;
- employee 1 displays `Unknown employee` and the department `Operations`.

Start the UI in another terminal:

```powershell
npm run dev
```

Open the URL printed by Vite (usually `http://127.0.0.1:5173/`). Vite proxies `/api` requests to the local API on port 5080.

## What this sample demonstrates—and does not

It demonstrates nullable JSON contract handling and a small set of regression tests. It does not provide runtime schema validation for arbitrary untrusted payloads, test authentication/authorization, certify an API contract, or simulate a live SharePoint/Power Apps integration. For production clients, prefer a canonical OpenAPI/schema source and generated or runtime-validated types where appropriate.
