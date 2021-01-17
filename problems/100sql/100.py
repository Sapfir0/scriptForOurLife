from generation import generate_sql_requests


if __name__ == "__main__":
    for request in generate_sql_requests():
        print(request)

