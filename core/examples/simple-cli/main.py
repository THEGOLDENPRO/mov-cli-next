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

    choice_list: list[Metadata] = []

    for index, search_result in enumerate(search_results):
        print(f"#{index + 1} - {search_result.title}")

        choice_list.append(search_result)

    choice = int(input("\n Enter choice (e.g. 1): "))
    metadata = choice_list[choice - 1]

    # TODO: find a way to tell the plugin what specific episode / season of this content we want 
    # if the metadata type is multi. I need a very elegant way of doing this in the entire mov-core 
    # codebase.
    media = api.watch(metadata)

    # TODO: complete the rest...