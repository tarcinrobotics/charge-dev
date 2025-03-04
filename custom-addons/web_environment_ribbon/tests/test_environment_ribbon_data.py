# Copyright 2019 Eric Lembregts
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests import common


class TestEnvironmentRibbonData(common.TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.env["ir.config_parameter"].set_param("ribbon.name", "Test Ribbon {db_name}")
        cls.env["ir.config_parameter"].set_param("ribbon.color", "#000000")
        cls.env["ir.config_parameter"].set_param("ribbon.background.color", "#fff")

    def test_environment_ribbon(self):
        """This test confirms that the data that is fetched by the javascript
        code is the right title and colors."""
        ribbon = self.env["web.environment.ribbon.backend"].get_environment_ribbon()

        expected_ribbon = {
            "name": f"Test Ribbon {self.env.cr.dbname}",
            "color": "#000000",
            "background_color": "#fff",
        }

        self.assertDictEqual(ribbon, expected_ribbon)
