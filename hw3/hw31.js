use school;

db.students.find().forEach(function(student) {
	var s = Array();
	for ( var i = 0; i < student.scores.length; i++) {
		s.push(student.scores[i].score);
	}
	s_min = Math.min.apply(Math, s);
	db.students.update({
		_id : student._id
	}, {
		$pull : {
			scores : {
				score : s_min
			}
		}
	});
})

db.students.find({_id:100}).pretty();

db.students.aggregate({
	'$unwind' : '$scores'
}, {
	'$group' : {
		'_id' : '$_id',
		'average' : {
			$avg : '$scores.score'
		}
	}
}, {
	'$sort' : {
		'average' : -1
	}
}, {
	'$limit' : 1
})