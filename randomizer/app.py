""" Module for loading the app UI """

import sys

from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout
from PyQt5.QtGui import QIcon

from ui_elements import label, spinbox, check_box, combo_box, button
from ui_elements.separator import create_v_sep, create_h_sep
from config import DEFAULT_CONFIG_PATH

APP = QApplication([])


class Randomizer(QWidget):
    """ Randomizer GUI """

    def __init__(self, parent=None, title="Randomizer"):
        super().__init__(parent)

        self.setWindowTitle(title)

        self.setWindowIcon(QIcon(f"{DEFAULT_CONFIG_PATH}/randomizer.ico"))

        self.labels = label.create_labels(self)
        self.spin_boxes = spinbox.create_spin_boxes(self)
        self.check_boxes = check_box.create_check_boxes(self.spin_boxes)
        self.combo_boxes = combo_box.create_combo_boxes()
        self.buttons = button.create_buttons(self)

        left_column = self.create_left_column()
        middle_column = self.create_middle_column()
        right_column = self.create_right_column()

        left_grid = QGridLayout()
        left_grid.addLayout(left_column, 1, 0)
        left_grid.addWidget(create_v_sep(self), 1, 1)
        left_grid.addLayout(middle_column, 1, 2)

        right_grid = QGridLayout()
        right_grid.addLayout(right_column, 0, 0)

        main_grid = QGridLayout(self)

        main_grid.addWidget(self.labels["randomize"], 0, 0)
        main_grid.addWidget(create_v_sep(self), 0, 1)
        main_grid.addWidget(self.labels["modify"], 0, 2)
        main_grid.addWidget(create_h_sep(self), 1, 0, 1, 0)
        main_grid.addLayout(left_grid, 2, 0)
        main_grid.addWidget(create_v_sep(self), 2, 1)
        main_grid.addLayout(right_grid, 2, 2)
        main_grid.addWidget(create_h_sep(self), 3, 0, 1, 0)
        main_grid.addWidget(self.buttons["randomize"], 4, 0)
        main_grid.addWidget(self.buttons["modify"], 4, 2)

        self.setLayout(main_grid)

    def create_left_column(self):
        """ Create the left column of the main grid """
        grid = QGridLayout()
        grid.addWidget(self.labels["bases"], 0, 0, 1, 0)
        grid.addWidget(create_h_sep(self), 1, 0, 1, 0)

        grid.addWidget(self.labels["playable_bases"], 2, 0)
        grid.addWidget(self.check_boxes["pb_enabled"], 2, 1)
        grid.addWidget(self.labels["pb_minimum"], 3, 0)
        grid.addWidget(self.spin_boxes["pb_min"], 3, 1)
        grid.addWidget(self.labels["pb_maximum"], 4, 0)
        grid.addWidget(self.spin_boxes["pb_max"], 4, 1)
        grid.addWidget(create_h_sep(self), 5, 0, 1, 0)

        grid.addWidget(self.labels["boss_bases"], 6, 0)
        grid.addWidget(self.check_boxes["bb_enabled"], 6, 1)
        grid.addWidget(self.labels["bb_minimum"], 7, 0)
        grid.addWidget(self.spin_boxes["bb_min"], 7, 1)
        grid.addWidget(self.labels["bb_maximum"], 8, 0)
        grid.addWidget(self.spin_boxes["bb_max"], 8, 1)
        grid.addWidget(create_h_sep(self), 9, 0, 1, 0)

        grid.addWidget(self.labels["other_bases"], 10, 0)
        grid.addWidget(self.check_boxes["ob_enabled"], 10, 1)
        grid.addWidget(self.labels["ob_minimum"], 11, 0)
        grid.addWidget(self.spin_boxes["ob_min"], 11, 1)
        grid.addWidget(self.labels["ob_maximum"], 12, 0)
        grid.addWidget(self.spin_boxes["ob_max"], 12, 1)
        grid.addWidget(create_h_sep(self), 13, 0, 1, 0)

        grid.addWidget(self.labels["class_bases"], 14, 0)
        grid.addWidget(self.check_boxes["cb_enabled"], 14, 1)
        grid.addWidget(self.labels["cb_minimum"], 15, 0)
        grid.addWidget(self.spin_boxes["cb_min"], 15, 1)
        grid.addWidget(self.labels["cb_maximum"], 16, 0)
        grid.addWidget(self.spin_boxes["cb_max"], 16, 1)

        return grid

    def create_middle_column(self):
        """ Create the middle column of the main grid """
        grid = QGridLayout()
        grid.addWidget(self.labels["growths"], 0, 0, 1, 0)
        grid.addWidget(create_h_sep(self), 1, 0, 1, 0)

        grid.addWidget(self.labels["playable_growths"], 2, 0)
        grid.addWidget(self.check_boxes["pg_enabled"], 2, 1)
        grid.addWidget(self.labels["pg_minimum"], 3, 0)
        grid.addWidget(self.spin_boxes["pg_min"], 3, 1)
        grid.addWidget(self.labels["pg_maximum"], 4, 0)
        grid.addWidget(self.spin_boxes["pg_max"], 4, 1)
        grid.addWidget(create_h_sep(self), 5, 0, 1, 0)

        grid.addWidget(self.labels["boss_growths"], 6, 0)
        grid.addWidget(self.check_boxes["bg_enabled"], 6, 1)
        grid.addWidget(self.labels["bg_minimum"], 7, 0)
        grid.addWidget(self.spin_boxes["bg_min"], 7, 1)
        grid.addWidget(self.labels["bg_maximum"], 8, 0)
        grid.addWidget(self.spin_boxes["bg_max"], 8, 1)
        grid.addWidget(create_h_sep(self), 9, 0, 1, 0)

        grid.addWidget(self.labels["other_growths"], 10, 0)
        grid.addWidget(self.check_boxes["og_enabled"], 10, 1)
        grid.addWidget(self.labels["og_minimum"], 11, 0)
        grid.addWidget(self.spin_boxes["og_min"], 11, 1)
        grid.addWidget(self.labels["og_maximum"], 12, 0)
        grid.addWidget(self.spin_boxes["og_max"], 12, 1)
        grid.addWidget(create_h_sep(self), 13, 0, 1, 0)

        grid.addWidget(self.labels["etc"], 14, 0, 1, 0)
        grid.addWidget(create_h_sep(self), 15, 0, 1, 0)
        grid.addWidget(self.labels["force_master_seal"], 16, 0)
        grid.addWidget(self.check_boxes["master_seal_enabled"], 16, 1)
        grid.addWidget(self.labels["class_mode"], 17, 0)
        grid.addWidget(self.combo_boxes["class_mode"], 17, 1)

        grid.addWidget(self.check_boxes["playable_class"], 18, 0)
        grid.addWidget(self.check_boxes["boss_class"], 18, 1)
        #        grid.addWidget(self.check_boxes["other_class"], 19, 0, 1, 0)
        grid.addWidget(self.check_boxes["other_class"], 19, 0)
        grid.addWidget(self.check_boxes["mix_promotes"], 19, 1)

        return grid

    def create_right_column(self):
        """ Create the right part of the main grid """
        grid = QGridLayout()
        grid.addWidget(self.labels["mod_bases"], 0, 0, 1, 0)
        grid.addWidget(create_h_sep(self), 1, 0, 1, 0)

        grid.addWidget(self.labels["mod_playable_bases"], 2, 0)
        grid.addWidget(self.check_boxes["mpb_enabled"], 2, 1)
        grid.addWidget(self.labels["mod_pb"], 3, 0)
        grid.addWidget(self.spin_boxes["pb_mod"], 3, 1)
        grid.addWidget(create_h_sep(self), 4, 0, 1, 0)

        grid.addWidget(self.labels["mod_boss_bases"], 5, 0)
        grid.addWidget(self.check_boxes["mbb_enabled"], 5, 1)
        grid.addWidget(self.labels["mod_bb"], 6, 0)
        grid.addWidget(self.spin_boxes["bb_mod"], 6, 1)
        grid.addWidget(create_h_sep(self), 7, 0, 1, 0)

        grid.addWidget(self.labels["mod_other_bases"], 8, 0)
        grid.addWidget(self.check_boxes["mob_enabled"], 8, 1)
        grid.addWidget(self.labels["mod_ob"], 9, 0)
        grid.addWidget(self.spin_boxes["ob_mod"], 9, 1)

        grid.addWidget(self.labels["mod_growths"], 10, 0, 1, 0)
        grid.addWidget(create_h_sep(self), 11, 0, 1, 0)

        grid.addWidget(self.labels["mod_playable_growths"], 12, 0)
        grid.addWidget(self.check_boxes["mpg_enabled"], 12, 1)
        grid.addWidget(self.labels["mod_pg"], 13, 0)
        grid.addWidget(self.spin_boxes["pg_mod"], 13, 1)
        grid.addWidget(create_h_sep(self), 14, 0, 1, 0)

        grid.addWidget(self.labels["mod_boss_growths"], 15, 0)
        grid.addWidget(self.check_boxes["mbg_enabled"], 15, 1)
        grid.addWidget(self.labels["mod_bg"], 16, 0)
        grid.addWidget(self.spin_boxes["bg_mod"], 16, 1)
        grid.addWidget(create_h_sep(self), 17, 0, 1, 0)

        grid.addWidget(self.labels["mod_other_growths"], 18, 0)
        grid.addWidget(self.check_boxes["mog_enabled"], 18, 1)
        grid.addWidget(self.labels["mod_og"], 19, 0)
        grid.addWidget(self.spin_boxes["og_mod"], 19, 1)

        return grid

    def start(self):
        """ Start the app """
        self.show()
        sys.exit(APP.exec_())
