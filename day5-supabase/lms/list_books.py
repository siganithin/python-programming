import os
from supabase import create_client
from dotenv import load_dotenv

load_dotenv()

sb = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))

resp = sb.table("books").select("*").order("book_id", desc=False).execute()

books = resp.data

if not books:
    print("No books found.")
else:
    print("ID | Title | Author | Category | Stock")
    for r in books:
        print(f"{r['book_id']} | {r['title']} | {r['author']} | {r.get('category', '-') or '-'} | {r['stock']}")
