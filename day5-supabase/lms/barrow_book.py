import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb = create_client(url, key)

def borrow_book(member_id, book_id):
    # 1. Get current stock
    book = sb.table("books").select("stock").eq("book_id", book_id).single().execute().data
    if not book:
        return {"success": False, "message": "Book not found"}
    if book["stock"] <= 0:
        return {"success": False, "message": "Book out of stock"}

    # 2. Reduce stock
    sb.table("books").update({"stock": book["stock"] - 1}).eq("book_id", book_id).execute()

    # 3. Insert borrow record
    sb.table("borrow_records").insert({"member_id": member_id, "book_id": book_id}).execute()

    return {"success": True, "message": "Book borrowed successfully"}

if __name__ == "__main__":
    member_id = int(input("Enter member ID: ").strip())
    book_id = int(input("Enter book ID: ").strip())
    result = borrow_book(member_id, book_id)
    print(result)
