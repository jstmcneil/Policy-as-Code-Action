import pymsteams
import sys

if (len(sys.argv) > 1):
	# You must create the connectorcard object with the Microsoft Webhook URL
	myTeamsMessage = pymsteams.connectorcard(sys.argv[1])
	myTeamsMessage.color("#00FF00")

	# Create message section
	myTeamsMessage.summary("**CFN-GUARD REPORT:**")
	myTeamsMessage.text("**CFN-GUARD REPORT:**")
	myMessageSection = pymsteams.cardsection()

	# Constructing the body of the message
	body = "All of your code templates have passed all configuration checks!"

	# Add text to the message.
	myMessageSection.activityText(body)
	myTeamsMessage.addSection(myMessageSection)

	# send the message.
	myTeamsMessage.send()
print("\033[32mPassed: \033[0mYour code templates have passed all configuration checks!")
