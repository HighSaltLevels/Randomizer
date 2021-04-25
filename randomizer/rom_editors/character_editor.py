""" Module for editing characters """

from random import randint

from constants import CLASS_MODE_COMBAT, CLASS_MODE_STAFF, CLASS_MODE_ALL

def randomize(status_label, game_config, rom_data, filters, class_mode, mix_promotes):
    """ Randomize based on the current status of the CONFIG """
    promoted, unpromoted = _get_class_list(game_config, rom_data, class_mode)
    class_list = []

    for character in game_config["classes"]["characters"]:
        character_data = game_config["classes"]["characters"][character]
        if character_data["kind"] not in filters:
            status_label.setText(f"Status: randomizing {character}")

            if mix_promotes:
                class_list = promoted + unpromoted
            else:
                class_list = promoted if rom_data[character_data["location"][0]] in promoted else unpromoted

            rand = randint(0, len(class_list) - 1)
            char_classes = character_data["location"]

            # Randomize the class
            for char_class in char_classes:
                rom_data[char_class] = rand

    return rom_data

def _get_class_list(game_config, rom_data, class_mode):
    promoted = []
    unpromoted = []
    class_ptr = 0
    class_stats = game_config["classes"]["class_stats"]

    first_class = class_stats["first"]
    for _class in range(class_stats["num_classes"]):
        if _class in class_stats["blacklist"]:
            continue

        if _class in class_stats["other"] and class_mode != CLASS_MODE_ALL:
            continue

        if _class in class_stats["staff_only"] and class_mode not in [CLASS_MODE_ALL, CLASS_MODE_STAFF]:
            continue

        prom_pos = rom_data[first_class + class_ptr + class_stats["promotion"]["offset"]]
        if int(prom_pos) & class_stats["promotion"]["bit_mask"] == 0:
            unpromoted.append(_class)

        else:
            promoted.append(_class)

    return promoted, unpromoted
