import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def delete_book(book_id):
    borrowed = sb.table("borrow_records").select("*").eq("book_id", book_id).is_("return_date", None).execute()
    if borrowed.data:
        return {"error": "Cannot delete book — it is currently borrowed."}

    resp = sb.table("books").delete().eq("book_id", book_id).execute()
    return resp.data

if __name__ == "__main__":
    book_id = int(input("Enter book ID: ").strip())
    deleted = delete_book(book_id)
    print("Deleted:", deleted)
