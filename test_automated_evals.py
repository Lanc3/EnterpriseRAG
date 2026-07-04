from run_evals import evaluate_generated_answer


def run_RAG(user_question):
    return "IDKLOL"

def test_run_RAG():
    evals = [
        {
            "question": "what is a node",
            "expected_answer": """A node is Godot's basic building block. Almost everything you place in a scene is a node: player, camera, sprite, button, light, collision shape, audio player, timer, and so on.
Godot scenes are trees of nodes. A scene might look like:
Player
-Sprite2D
-CollisionShape2D
-Camera2D""",
        },
        {
            "question": "where do i set positions of a node",
            "expected_answer": """It depends what kind of node it is:
For 2D game objects, use Node2D position fields:
position = Vector2(100, 200)
global_position = Vector2(100, 200)
position is relative to the parent. global_position is relative to the whole world/viewport.

For 3D game objects, use Node3D position fields:
position = Vector3(0, 1, 5)
global_position = Vector3(0, 1, 5)
Node3D.position is relative to the parent; global_position is relative to the world.

For UI nodes, use Control layout properties: position, global_position, size, anchors, offsets, and containers.
In the editor, select the node, then use the Inspector on the right. For 2D/3D nodes, look under Transform. For UI nodes, look under layout/anchors/offsets.""",
        },
        {
            "question": "what nodes exist and what do they do",
            "expected_answer": "",
        },
    ]

    failures = []

    for eval_case in evals:
        question = eval_case["question"]
        expected_answer = eval_case["expected_answer"]

        generated_answer = run_RAG(question)

        deepseek_response = evaluate_generated_answer(
            expected_answer=expected_answer,
            generated_answer=generated_answer,
        )

        passed = "RESULT: PASS" in deepseek_response.upper()

        if not passed:
            failures.append(
                f"""
================ RAG EVAL FAILED ================

QUESTION:
{question}

EXPECTED ANSWER:
{expected_answer}

GENERATED RAG ANSWER:
{generated_answer}

DEEPSEEK JUDGE RESPONSE:
{deepseek_response}

=================================================
"""
            )

    assert not failures, "\n\n".join(failures)