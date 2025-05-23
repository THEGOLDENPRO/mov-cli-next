import sys

from mov_core.api.v1 import API, Metadata

if __name__ == "__main__":
    api = API()

    # Let's use the second argument as the query...

    cli_args = iter(sys.argv)
    next(cli_args) # consume the first arg

    query = next(cli_args, None)

    if query is None:
        print("No search query was passed!")
        exit(1)

    search_results = api.search(query)

    for index, search_result in enumerate(search_results):
        print(f"#{index + 1} - {search_result.name}")

    choice = input("\n Enter choice (e.g. 1): ")

    # TODO: complete all of this when API is implemented.
    search_result: Metadata = ...

    api.watch(search_result)