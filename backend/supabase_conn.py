import os
from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


def main():

    print(f"url is: {url}")
    response = supabase.table('countries').select("*").execute()
    print(response)



if __name__ == "__main__":
    main()