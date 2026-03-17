import pandas as pd

tables = pd.read_html("https://www.laspositascollege.edu/adminservices/payrollandhiring.php")
df = tables[0]

html = f"""<!DOCTYPE html>
<html>
<head>
    <title>LPC Payroll Schedule</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 40px auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        h1 {{
            color: #2c3e50;
            text-align: center;
        }}
        .updated {{
            text-align: center;
            color: #888;
            margin-bottom: 20px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            background: white;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        th {{
            background-color: #2c3e50;
            color: white;
            padding: 12px 15px;
            text-align: left;
        }}
        td {{
            padding: 10px 15px;
            border-bottom: 1px solid #eee;
        }}
        tr:hover {{
            background-color: #f0f7ff;
        }}
    </style>
</head>
<body>
    <h1>LPC Payroll Schedule</h1>
    <p class="updated">Auto-updated from LPC website</p>
    {df.to_html(index=False, classes="schedule")}
</body>
</html>"""

with open("index.html", "w") as f:
    f.write(html)

print("Page updated!")