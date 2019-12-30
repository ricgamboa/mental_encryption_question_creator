# Main program that create a new question

import def_classes


def main():
    COLLECTION_SIZE = 100
    NUM_ICONS_SENDER = 5
    POSITION_LIST_SIZE = 15

    # question id definition
    current_id = input("question id: ")

    # define how many letters will receive will have the answer
    num_answer_letters = int(input("how many letters must have the answer: "))

    current_question = def_classes.Question(current_id, num_answer_letters)

    # create one set of icons with random order for each letter
    icons = def_classes.Icons(COLLECTION_SIZE)
    for count_sets in range(current_question.num_answer_letters):
        current_question.append_icon_set(icons.random_order())

    #create one list with random positions for each letter
    for count_pos in range(current_question.num_answer_letters):
        position = def_classes.PositionList(POSITION_LIST_SIZE, NUM_ICONS_SENDER)
        current_question.append_position_list(position.list)

    #save question to database
    current_question.save_info()


if __name__ == "__main__":
    main()
