var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/health", () => Results.Ok(new { status = "ok" }));

app.MapGet("/api/employees/{id:int}", IResult (int id) =>
{
    // Synthetic data only. The nullable display name for employee 1 is intentional.
    EmployeeDto? employee = id switch
    {
        1 => new EmployeeDto(1, null, "Operations"),
        2 => new EmployeeDto(2, "Asha Rao", "Engineering"),
        _ => null
    };

    return employee is null ? Results.NotFound() : Results.Ok(employee);
});

app.Run();

// ASP.NET Core's default JSON naming policy serializes these properties as camelCase.
public sealed record EmployeeDto(int Id, string? DisplayName, string Department);
