# License LGPL-3.0 or later (http://www.gnu.org/licenses/LGPL).


from requests import Response

from fastapi import status

from ..routers import demo_router
from .common import FastAPITransactionCase


class FastAPIMultiSlashDemoCase(FastAPITransactionCase):
    """
    This test verifies that multi-slash endpoint are properly reached
    """

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.default_fastapi_router = demo_router
        cls.default_fastapi_running_user = cls.env.ref(
            "fastapi.fastapi_endpoint_multislash_demo"
        )
        cls.default_fastapi_authenticated_partner = cls.env["res.partner"].create(
            {"name": "FastAPI Demo"}
        )

    def test_hello_world(self) -> None:
        with self._create_test_client() as test_client:
            response: Response = test_client.get("/demo/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertDictEqual(response.json(), {"Hello": "World"})
