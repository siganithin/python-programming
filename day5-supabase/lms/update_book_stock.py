import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def update_book_stock(book_id, new_stock):
    payload = {"stock": new_stock}
    resp = sb.table("books").update(payload).eq("book_id", book_id).execute()
    return resp.data

if __name__ == "__main__":
    book_id = int(input("Enter book ID: ").strip())
    new_stock = int(input("Enter new stock: ").strip())
    updated = update_book_stock(book_id, new_stock)
    print("Updated:", updated)
