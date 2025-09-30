from Spotfire.Dxp.Data import DataValueCursor

# List of accounts and matching property suffixes
accounts = {
    "S0099-Critical Stat": "S0099",
    "S0152-Total Procedures": "S0152",
    "Total Visits": "Visits",
    "Net Revenue": "Revenue",
    "Salaries, Wages & Benefits": "SWB",
    "Gain/(Loss) from Operations": "GainLoss",
    "Total EBITDA Expenses": "EBITDA"
}

# Create formatted cursors
account_cursor = DataValueCursor.CreateFormatted(data_table.Columns["AccountsWithPlaceHolders"])
mth1_cursor = DataValueCursor.CreateFormatted(data_table.Columns["CA_FirstMthValue"])
mth2_cursor = DataValueCursor.CreateFormatted(data_table.Columns["CA_SecondMthValue"])
mth3_cursor = DataValueCursor.CreateFormatted(data_table.Columns["CA_ThirdMthValue"])

# Reset cursors
account_cursor.Reset()
mth1_cursor.Reset()
mth2_cursor.Reset()
mth3_cursor.Reset()

# Loop through rows
for row in data_table.GetRows():
    account_cursor.MoveNext()
    mth1_cursor.MoveNext()
    mth2_cursor.MoveNext()
    mth3_cursor.MoveNext()

    acct = account_cursor.CurrentValue
    if acct in accounts:
        suffix = accounts[acct]
        Document.Properties["CA_FirstMth_" + suffix] = float(mth1_cursor.CurrentValue)
        Document.Properties["CA_SecondMth_" + suffix] = float(mth2_cursor.CurrentValue)
        Document.Properties["CA_ThirdMth_" + suffix] = float(mth3_cursor.CurrentValue)
