require 'aws-sdk-dynamodb'

def worker(event:, context:)
  event["Records"].each do | record |
    if not record["eventName"] == "INSERT":
      next
    end

    image = record["dynamodb"]["NewImage"]
    scan_id = image["id"]["S"]
    target = image["target"]["S"]
    port = image["port"]["N"]).to_i

    # TODO: Add real scan logic here to populate scan var, probably via a scan-engine
    scan = {
        'target': target,
        'port': port,
        'foo': 'bar'
    }
    sleep(5)

    dynamodb = Aws::DynamoDB::Client.new(region: 'us-west-2')

    dynamodb.update_item({
      expression_attribute_names: {
        "#st" => "status", 
        "#sc" => "scan", 
      }, 
      expression_attribute_values: {
        ":st" => {
          s: "COMPLETED", 
        }, 
        ":sc" => scan, 
      }, 
      key: {
        "id" => {
          s: scan_id, 
        }
      }, 
      table_name: ENV['DYNAMODB_TABLE'], 
      update_expression: "SET #statusresult = :st, #scanresult = :sc", 
    })
  end
end