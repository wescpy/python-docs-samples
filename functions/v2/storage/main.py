# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


# [START functions_cloudevent_storage]
# Triggered by a change in a storage bucket
def hello_gcs(cloudevent):
    data = cloudevent.data

    event_id = cloudevent["id"]
    event_type = cloudevent["type"]

    bucket = data["bucket"]
    name = data["name"]
    metageneration = data["metageneration"]
    timeCreated = data["timeCreated"]
    updated = data["updated"]

    print('Event ID: {}'.format(event_id))
    print('Event type: {}'.format(event_type))
    print('Bucket: {}'.format(bucket))
    print('File: {}'.format(name))
    print('Metageneration: {}'.format(metageneration))
    print('Created: {}'.format(timeCreated))
    print('Updated: {}'.format(updated))
# END functions_cloudevent_storage
