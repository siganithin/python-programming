import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def delete_member(member_id):
    borrowed = sb.table("borrow_records").select("*").eq("member_id", member_id).is_("return_date", None).execute()
    if borrowed.data:
        return {"error": "Cannot delete member — they still have borrowed books."}

    resp = sb.table("members").delete().eq("member_id", member_id).execute()
    return resp.data

if __name__ == "__main__":
    member_id = int(input("Enter member ID: ").strip())
    deleted = delete_member(member_id)
    print("Deleted:", deleted)
