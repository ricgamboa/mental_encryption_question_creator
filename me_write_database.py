# This module must be replaced by database integration
# communication with user database must have very strong security and authentication


from pathlib import Path


def save_sender(sid, name, icons, cell):
    database_path = Path.cwd().joinpath("project_files", "users_database")
    database_append = open(database_path, "a")
    database_append.write('{"user_id":' + sid + ', "user_name":"' + name + '"' + ', "user_icons":' + icons + ', "user_cell":' + cell + '}\n')
    database_append.close()

def save_question(qid, num_letters, icons, pos_list):
    database_path = Path.cwd().joinpath("project_files", "question_database")
    database_append = open(database_path, "a")
    count = 0
    list_icons = ""
    for ic in icons:
        if count < 1: list_icons = '{"icon_list":' + ic + "}"
        else: list_icons += ', {"icon_list":' + ic + "}"
        count += 1
    list_icons = "[" + list_icons + "]"
    count = 0
    position_list = ""
    for pl in pos_list:
        if count < 1: position_list = '{"position_list":' + pl + "}"
        else: position_list += ', {"position_list":' + pl + "}"
        count += 1
    position_list = "[" + position_list + "]"
    database_append.write('{"question_id":' + qid + ', "number_letters":' + num_letters + ', "icons_lists_all":' + list_icons + ', "positions_lists_all":' + position_list + '}\n')
    database_append.close()
