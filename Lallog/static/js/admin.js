$(function() {
				$("#export").click(function(e){
						$("#result").table2excel({
							name: "Excel Document Name",
							filename: "myFileName" + new Date().toISOString().replace(/[\-\:\.]/g, "") + ".xls",
							fileext: ".xls",
						});

				});

			});