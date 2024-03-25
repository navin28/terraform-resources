import base64
import json
import os

from google.cloud import pubsub_v1


# TODO(developer): set this environment variable
PROJECT_ID = "kodekloud-389817" #os.getenv("GOOGLE_CLOUD_PROJECT")


# Instantiates a Pub/Sub client
publisher = pubsub_v1.PublisherClient()


# Publishes a message to a Cloud Pub/Sub topic.
def publish(request):
    request_json = request.get_json(silent=True)

    topic_name = request_json.get("pub-test-py-local")
    message = request_json.get("Hello World!")

    if not topic_name or not message:
        return ('Missing "topic" and/or "message" parameter.', 400)

    print(f"Publishing message to topic {topic_name}")

    # References an existing topic
    topic_path = publisher.topic_path(PROJECT_ID, topic_name)

    message_json = json.dumps(
        {
            "data": {"name": message},
        }
    )
    message_bytes = message_json.encode("utf-8")

    # Publishes a message
    try:
        publish_future = publisher.publish(topic_path, data=message_bytes)
        publish_future.result()  # Verify the publish succeeded
        return "Message published."
    except Exception as e:
        print(e)
        return (e, 500)

# from google.cloud import pubsub_v1

# # (developer)
# project_id = "kodekloud-389817"

# publisher = pubsub_v1.PublisherClient()
# project_path = f"projects/{project_id}"

# for topic in publisher.list_topics(request={"project": project_path}):
#     print(topic)

# from google.cloud import pubsub_v1

# # (developer)
# project_id = "kodekloud-389817"
# topic_id = "pub-test-py-local"

# publisher = pubsub_v1.PublisherClient()
# topic_path = publisher.topic_path(project_id, topic_id)

# topic = publisher.create_topic(request={"name": topic_path})

# print(f"Created topic: {topic.name}")


# # requirements.txt
# # google-api-core==1.31.1
# # google-cloud-pubsub==2.7.0
# #main.py
# import os
# import json
# from google.cloud import pubsub_v1

# def hello_world(request): 
#     request_json = request.get_json()
#     publisher = pubsub_v1.PublisherClient()
#     topic_name = 'projects/{project_id}/topics/{topic}'.format(project_id=os.getenv('GOOGLE_CLOUD_PROJECT'),topic='attendance-events')

#     publisher.create_topic(name=topic_name)

#     data = json.dumps(request_json).encode("utf-8")           
#     future = publisher.publish(topic_name, data=data)
#     future.result()

# #### Stack trace
# #2021-08-13 17:52:54.953 ISTtestpublish Traceback (most recent call last): File "/layers/google.python.pip/pip/bin/functions-framework", line 8, in <module> sys.exit(_cli()) File "/layers/google.python.pip/pip/lib/python3.9/site-packages/click/core.py", line 829, in __call__ return self.main(*args, **kwargs) File "/layers/google.python.pip/pip/lib/python3.9/site-packages/click/core.py", line 782, in main rv = self.invoke(ctx) File "/layers/google.python.pip/pip/lib/python3.9/site-packages/click/core.py", line 1066, in invoke return ctx.invoke(self.callback, **ctx.params) File "/layers/google.python.pip/pip/lib/python3.9/site-packages/click/core.py", line 610, in invoke return callback(*args, **kwargs) File "/layers/google.python.pip/pip/lib/python3.9/site-packages/functions_framework/_cli.py", line 37, in _cli app = create_app(target, source, signature_type) File "/layers/google.python.pip/pip/lib/python3.9/site-packages/functions_framework/__init__.py", line 237, in create_app spec.loader.exec_module(source_module) File "<frozen importlib._bootstrap_external>", line 850, in exec_module File "<frozen importlib._bootstrap>", line 228, in _call_with_frames_removed File "/workspace/main.py", line 4, in <module> from google.cloud import pubsub_v1 ImportError: cannot import name 'pubsub_v1' from 'google.cloud' (unknown location)
# # example