import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
sb: Client = create_client(url, key)

def update_member_email(member_id, new_email):
    payload = {"email": new_email}
    resp = sb.table("members").update(payload).eq("member_id", member_id).execute()
    return resp.data

if __name__ == "__main__":
    member_id = int(input("Enter member ID: ").strip())
    new_email = input("Enter new email: ").strip()
    updated = update_member_email(member_id, new_email)
    print("Updated:", updated)
