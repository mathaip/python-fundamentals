import sqlite3

conn = sqlite3.connect('chinook.db')
print ("Opened database successfully")

# cursor_1 = conn.execute("SELECT FirstName, LastName,CustomerId, Country FROM Customers WHERE Country != ('UnitedStates') ")   
# for row in cursor_1:
#    print ("FirstName = ",row[0])
#    print ("LastName = ",row[1])
#    print ("CustomerId = ", row[2])
#    print ("Country = ", row[3], "\n")

# cursor_2 = conn.execute("SELECT FirstName, LastName,CustomerId, Country FROM Customers WHERE Country = ('Brazil') ")   
# for row in cursor_2:
#    print ("FirstName = ",row[0])
#    print ("LastName = ",row[1])
#    print ("CustomerId = ", row[2])
#    print ("Country = ", row[3], "\n")

# cursor_3 = conn.execute("SELECT FirstName, LastName, Country, InvoiceId, Dateofinvoice FROM Customers LEFT JOIN Invoices WHERE Country = ('Brazil') ")
# for row in cursor_3:
#    print ("FirstName = ",row[0])
#    print ("LastName = ",row[1])
#    print ("InvoiceId = ", row[2])
#    print ("Date_of_invoice = ", row[3]) 
#    print ("BillingCountry = ", row[4], "\n")

# cursor_4 = conn.execute("SELECT FirstName, LastName,Title FROM Employees WHERE Title = ('SalesManager') or  ")   
# for row in cursor_4:
#    print ("FirstName = ",row[0])
#    print ("LastName = ",row[1])
#    print ("SalesAgent = ", row[2], "\n")

# cursor_5 = conn.execute("SELECT BillingCountry FROM Invoices") 
# for row in cursor_5:
#    print ("BillingCountry = ",row[0])

# cursor_6 = conn.execute("SELECT * FROM Customers INNER JOIN Invoices") \
# print("FirstName = ",row[0])
# print("LastName = ",row[1])
# print ("Country = ", row[2], "\n")


# #13.

# cursor_7= conn.execute("SELECT Count (InvoiceId) AS NumberOfInvoices, BillingCountry FROM Invoices GROUPBY BillingCountry")


# last question
# 1) media_types.mediaTypeId
# 2) tracks.mediaTypeId
# 3) invoice_items.trackId
cursor_8= conn.execute("SELECT SUM (invoices.Total) AS TotalSales, tracks.Name, media_types.Name AS MediaType From Invoice_Items \
	INNER JOIN tracks ON tracks.TrackId = Invoice_Items.TrackId \
	INNER JOIN invoices ON invoices.InvoiceId = Invoice_Items.InvoiceId \
	INNER JOIN media_types ON media_types.MediaTypeId = tracks.MediaTypeID \
	GROUP BY tracks.Name \
	ORDER BY totalsales DESC\
	 LIMIT 1")

for row in cursor_8:
	print("TotalSales = ",row[0])
 	print("tracks.Name = ",row[1])
 	print ("MediaType = ", row[2], "\n")

conn.commit()
