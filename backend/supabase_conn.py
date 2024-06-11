import os
from supabase import create_client, Client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

def main():

    print(f"url is: {url}")
    response = supabase.table('Prep_QnA').select("*").execute()
    print(response)


    print("----------------------------------")





def insert():
    ## test insert data to countries table

    data, count = ((supabase.table('countries')
                    .insert({"name": "Kenya"}))
                   .execute())

    print(data)
    print(count)




if __name__ == "__main__":
    main()
    insert()