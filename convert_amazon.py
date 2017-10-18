import pandas as pd

FILE_PATH = r'C:\Users\jt\Downloads\ProductDetails (1).csv'

INITIAL_COLUMNS = ['ASIN', 'ASIN name', 'ID type', 'External ID', 'Product group',
       'Released', 'Customer orders', 'Units shipped', 'Free replacements',
       'Shipped COGS', 'Units at Amazon', 'Sellable on hand cost',
       'Unsellable units at Amazon', 'Vendor units received', 'Open PO qty',
       'Unfilled customer orders', 'Customer returns', 'Category',
       'Subcategory', 'Model number', 'Catalog number', 'Replenishment code',
       'Author / Artist', 'Binding', 'Format', 'Brand code']
DESIRED_COLUMNS = ['ASIN name','Units shipped','Units at Amazon','Open PO qty']


def convert_to_isbn13(s):
    """ Converts individual value ISBN10s to ISBN13s. """

    calc = 38 + 3 * int(s[0]) + int(s[1]) + 3 * int(s[2]) + int(
        s[3]) + 3 * int(s[4]) + int(s[5]) + 3 * int(s[6]) + int(
        s[7]) + 3 * int(s[8])

    if 10 - (calc % 10) == 10:
        check = "0"
    else:
        check = str(10 - (calc % 10))

    return "978" + s[0:9] + check


def isbn10_to_13(isbn):
    """ Used as a converter in the df creation step."""
    if len(isbn) == 13:
        return isbn

    if len(isbn)<10:
        isbn = "0{}".format(isbn)
        return convert_to_isbn13(isbn)

    if len(isbn) == 10:
        return convert_to_isbn13(isbn)


df = pd.DataFrame(pd.read_csv(FILE_PATH,skiprows=8,
                              converters={'External ID' : isbn10_to_13}))
df = df.set_index('External ID')
df.index.name = 'ISBN13'
df = df[DESIRED_COLUMNS]
df.columns = ['Title','Amazon_TW','Amazon_OH','Amazon_OO']

print(df.head(20))

