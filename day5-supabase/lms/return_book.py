import os
from supabase import create_client
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb = create_client(url, key)

def return_book(member_id, book_id):
    # 1. Mark record as returned
    sb.table("borrow_records")\
        .update({"return_date": datetime.now().isoformat()})\
        .eq("member_id", member_id)\
        .eq("book_id", book_id)\
        .is_("return_date", None)\
        .execute()

    # 2. Increase stock
    book = sb.table("books").select("stock").eq("book_id", book_id).single().execute().data
    sb.table("books").update({"stock": book["stock"] + 1}).eq("book_id", book_id).execute()

    return {"success": True, "message": "Book returned successfully"}

if __name__ == "__main__":
    member_id = int(input("Enter member ID: ").strip())
    book_id = int(input("Enter book ID: ").strip())
    result = return_book(member_id, book_id)
    print(result)
