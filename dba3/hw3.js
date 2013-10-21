//HW3.1

db.zips.aggregate([{$group:{_id:"$state",zips:{$sum:1}}},{$sort:{"zips":-1}},{$limit:10}])

//HW3.2

db.zips.aggregate( 
[
	{ $project : { _id : { $substr : ["$_id",0,1] } } } , 
	{ $group : { _id : "$_id", n : {$sum:1} } }
]
)
db.zips.aggregate( [ {$match:{city:{$regex:/[0-9].*/}}},{$group:{_id:{$substr:["$city",0,1]},n:{$sum:1}}} ] )

db.zips.remove({city:{$regex:/[0-9].*/}})
db.zips.count()

//HW3.4
db.zips.mapReduce(map_closest,function(city,i){return Array.sum(i)} ,{query:{state:"PA"},out:"closest_cities"})