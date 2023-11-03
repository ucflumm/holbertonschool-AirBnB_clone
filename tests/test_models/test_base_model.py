import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests for the BaseModel class"""

    def setUp(self):
        """Init Basemodel"""
        self.bm = BaseModel()

    def test_init(self):
        """Test init of BaseModel"""
        self.assertIsInstance(self.bm, BaseModel)

    def test_str(self):
        """Test __str__ method"""
        expected_val = (
            f"[{self.bm.__class__.__name__}] ({self.bm.id}) "
            f"{{'id': '{self.bm.id}', "
            f"'created_at': '{self.bm.created_at.isoformat()}', 'updated_at': "
            f"'{self.bm.updated_at.isoformat()}', '__class__': "
            f"'{type(self.bm).__name__}'}}"
        )
        self.assertEqual(str(self.bm), expected_val)

    def test_save(self):
        """Test save method"""
        origin_update_at = self.bm.updated_at
        self.bm.save()
        after_save_update_at = self.bm.updated_at
        self.assertNotEqual(origin_update_at, after_save_update_at)

    def test_save_alt(self):
        """Test save method"""
        bm_base = BaseModel()
        old_save = str(bm_base.updated_at)
        bm_base.save()
        update_save = str(bm_base.updated_at)
        self.assertNotEqual(old_save, update_save)


    def test_to_dict(self):
        """Test to_dict method"""
        created_at = self.bm.created_at.isoformat()
        updated_at = self.bm.updated_at.isoformat()
        new_dict = self.bm.to_dict()
        self.assertEqual(new_dict["created_at"], created_at)
        self.assertEqual(new_dict["updated_at"], updated_at)
        self.assertEqual(new_dict["__class__"], type(self.bm).__name__)
