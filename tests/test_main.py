import unittest
from main import cluster_texts, similarity, tfidf_vectors

class FeedbackClusterTests(unittest.TestCase):
    def test_groups_near_duplicate_feedback(self):
        docs = ["login password reset failure", "password reset login failure issue", "weather is sunny today"]
        groups = cluster_texts(docs, 0.2)
        self.assertEqual(sorted(len(group) for group in groups), [1, 2])

    def test_rejects_invalid_threshold(self):
        with self.assertRaises(ValueError):
            cluster_texts(["one"], 1.5)

if __name__ == "__main__":
    unittest.main()
