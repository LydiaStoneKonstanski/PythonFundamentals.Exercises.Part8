import os
def write_list_to_file(lines, file_path):
    file = open(file_path, 'w')
    for line in lines:
        file.write(line)
        file.write("\n")
    file.close()

def explore_directory(folder_path):
    tree_list = []
    for root, directories, files in os.walk(folder_path):
        # print(root)
        # print(files)
        for file in files:
            tree_list.append(root + "/" + file)

    return tree_list


if __name__=="__main__":
    sample_folder = "/Users/lydia/Documents/Books"
    output_file = "test_file.txt"
    tree_list = explore_directory(sample_folder)
    write_list_to_file(tree_list, output_file)

