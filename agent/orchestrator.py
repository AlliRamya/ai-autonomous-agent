from agent.planner import planner
from agent.executor import executor
from agent.reflection import reflection
from tools.document import document_generator


class AutonomousAgent:

    def run(self, request):

        print("\n========== AUTONOMOUS AGENT ==========\n")

        # --------------------------
        # STEP 1 : Planning
        # --------------------------

        print("Planning...")

        plan = planner.create_plan(request)

        print(plan)

        # --------------------------
        # STEP 2 : Execute
        # --------------------------

        print("\nExecuting tasks...")

        document = executor.execute(
            request,
            plan["tasks"]
)


        # --------------------------
        # STEP 3 : Reflection
        # --------------------------

        print("\nReviewing document...")

        review = reflection.review(document)

        if review != "PASS":

            print("Reflection requested improvements.")

            # If your Executor class has improve()
            if hasattr(executor, "improve"):
                document = executor.improve(
                    request,
                    document,
                    review
                )

        # --------------------------
        # STEP 4 : Generate Word
        # --------------------------

        filepath = document_generator(
            title=plan["document_type"],
            document_data=document
        )

        # --------------------------
        # STEP 5 : Return
        # --------------------------

        return {
            "status": "SUCCESS",
            "request": request,
            "document_type": plan["document_type"],
            "tasks": plan["tasks"],
            "document_path": filepath
        }


agent = AutonomousAgent()