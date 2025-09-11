from file_functions import FileFunctions

def main():

    file_path = r"C:/Users/USER/Documents/andmetarkus/Python/day-2/ANALYSIS/request-log.txt"

    # filecontent = ""

    # with open("request-log.txt", encoding="utf-8") as f:
        # filecontent = f.read()

    # request_log_entries = filecontent.split("\n")

    request_log_entries = FileFunctions().read_file(file_path)

    for line in request_log_entries:
        print(line + "\n")

    row_count = len(request_log_entries)
    print(f"Ridade arv: {row_count}")

    # with open("request-log.txt", "a") as f:  # a on append, lisab faili lõppu teksti. w kirjutab kõik üle
        # f.write("\nRidade arv: " + str(row_count) + "\n")

    FileFunctions().add_line_to_file(file_path, f"Logifailis on nüüd {row_count} rida.")



    

if __name__ == "__main__":
    main()