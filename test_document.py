from tools.document import document_generator


test_data = {

    "Introduction": 
    "This document is generated using Autonomous AI Agent.",


    "Features":
    [
        "AI Planning",
        "Task Execution",
        "Automatic Document Generation"
    ],


    "Conclusion":
    "The agent successfully created this document."

}



filepath = document_generator(

    title="AI_Agent_Test_Document",

    document_data=test_data

)


print("Document created:")
print(filepath)