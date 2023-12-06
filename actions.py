from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import psycopg2

class SaveQuestionToDatabase(Action):
    def name(self):
        print("step1")
        return "action_save_question_to_database"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain):
        message = tracker.latest_message.get("text")

        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="december9",
            host="127.0.0.1",
            port="5432"
        )

        # Create a cursor
        cursor = conn.cursor()

        # Insert the question into the database
        insert_query = "INSERT INTO chat_questions (message) VALUES (%s);"
        cursor.execute(insert_query, (message,))

        # Commit the transaction and close the cursor and connection
        conn.commit()
        cursor.close()
        conn.close()

        dispatcher.utter_message("I've saved your question to the database.")

        return []