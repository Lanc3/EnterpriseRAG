from run_evals import evaluate_generated_answer

def run_RAG(user_question):
    return "IDKLOL"

def test_run_RAG():
    evals_questions = [
    "what is a node",
    "where do i set positions of a node",
    "what nodes exist and what do they do",
    ]

    eval_answers = [
    '''A node is Godot's basic building block. Almost everything you place in a scene is a node: player, camera, sprite, button, light, collision shape, audio player, timer, and so on.
    Godot scenes are trees of nodes. A scene might look like:
    Player
    -Sprite2D
    -CollisionShape2D
    -Camera2D''',
        '''It depends what kind of node it is:
    For 2D game objects, use Node2D position fields:
    position = Vector2(100, 200)
    global_position = Vector2(100, 200)
    position is relative to the parent. global_position is relative to the whole world/viewport. Node2D is the base for most 2D nodes like sprites and 2D physics bodies. Node2D docs
    For 3D game objects, use Node3D position fields:
    position = Vector3(0, 1, 5)
    global_position = Vector3(0, 1, 5)
    Node3D.position is relative to the parent; global_position is relative to the world. Node3D docs
    For UI nodes, use Control layout properties: position, global_position, size, anchors, offsets, and containers. UI is a little different because it often responds to screen size and parent layout. Control docs
    In the editor, select the node, then use the Inspector on the right. For 2D/3D nodes, look under Transform. For UI nodes, look under layout/anchors/offsets.''',
        "",
    ]
    generated_answers = []
    for question in evals_questions:
        answer = run_RAG(question)
        generated_answers.append(answer)

    for i in range(len(evals_questions)):
        results = evaluate_generated_answer(eval_answers[i],generated_answers[i])
        assert "PASS" in results