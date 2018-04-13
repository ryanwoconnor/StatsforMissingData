import splunk
import splunk.admin as admin
import splunk.rest
import json
import requests
import sys
import splunk.Intersplunk 
#import splunk.mining.dcutils as dcu
 
#logger = dcu.getLogger()
 
#results = previous data in the search pipe
#settings = splunk 'header'
#logger.info(sessionKey) #logs sessionKey to python.log
#logger.info(results()[0]["_raw"]) #logs 1st result's _raw field to python.log


results,unused1,settings = splunk.Intersplunk.getOrganizedResults()
sessionKey = settings.get("sessionKey")
# for each results, add a 'shape' attribute, calculated from the raw event text
for result in results:
	result["success"] = "Succesfully Updated Macro"
# output results
#splunk.Intersplunk.outputResults(results)


#return modified search results back to splunk search pipeline



#example REST post using sessionKey
headers = {'Authorization':''}
headers['Authorization'] = 'Splunk ' + settings.get("sessionKey")  
data = {'definition':results[0]["definition"]}
r = requests.post("https://localhost:8089/servicesNS/nobody/StatsforMissingData/configs/conf-macros/missingdatasearchterms", headers=headers, data=data, verify=False)
splunk.Intersplunk.outputResults(results)
