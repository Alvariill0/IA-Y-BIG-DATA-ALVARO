{
    $match: {
      name: { $ne: "" }
    }
  },
  {
    $unwind: "$grades"
  },
  {
    $group: {
      _id: "$_id",
      nombre: { $first: "$name" },
      puntuacionTotal: { $sum: "$grades.score" }
    }
  },
  {
    $sort: {
      puntuacionTotal: -1
    }
  },
  {
    $limit: 5
}
