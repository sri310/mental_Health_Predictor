 $(document).ready(function(){
            console.log("ready");

                $("form").on("submit", function() {
                    console.log("form_submitted")


                    var q1 = $('#q1-0').val()
                    var q2 = $('#q2-0').val()
                    var q3 = $('#q3-0').val()
                    var q4 = $('#q4-0').val()
                    var q5 = $('#q5-0').val()
                    var q6 = $('#q6-0').val()
                    var q7 = $('#q7-0').val()
                    var q8 = $('#q8-0').val()
                    var q9 = $('#q9-0').val()
                    var q10 = $('#q10-0').val()
                    var q11 = $('#q11-0').val()
                    var q12 = $('#q12-0').val()
                    var q13 = $('#q13-0').val()
                    var q14 = $('#q14-0').val()
                    var q15 = $('#q15-0').val()
                    data = {q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15}

                    console.log(q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15)
                    var csrftoken = $('meta[name=csrf-token]').attr('content')

                    $.ajaxSetup({
                        beforeSend: function(xhr, settings) {
                            if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                                xhr.setRequestHeader("X-CSRFToken", csrftoken)
                            }
                        }
                    })

                    $.ajax({
                        type: "POST",
                        url : "/",
                        data: $('form').serialize(),
                        success : function(results){
                                    console.log(results);


                                    if(results.result =='Optimistic and happy with life'){
                                        $('.positiveAlert').text(' You are optimistic and happy with life').show();
                                        $('.negativeAlert').hide();
                                        $('.neutraleAlert').hide();
                                    }
                                    else if (results.result =='Unaffected about life'){
                                         $('.neutralAlert').text('You are unaffected about life').show();
                                         $('.negativeAlert').hide();
                                         $('.positiveAlert').hide();
                                     }
                                     else if (results.result  =='Mentally distressed'){
                                           $('.negativeAlert').text('You are mentally distressed').show();
                                           $('.neutralAlert').hide();
                                           $('.positiveAlert').hide();

                                     }
                                     else{
                                        console.log("something went wrong");
                                     }


                                    $('input[name=q1]').attr('checked',false);
                                    $('input[name=q2]').attr('checked',false);
                                    $('input[name=q3]').attr('checked',false);
                                    $('input[name=q4]').attr('checked',false);
                                    $('input[name=q5]').attr('checked',false);
                                    $('input[name=q6]').attr('checked',false);
                                    $('input[name=q7]').attr('checked',false);
                                    $('input[name=q8]').attr('checked',false);
                                    $('input[name=q9]').attr('checked',false);
                                    $('input[name=q10]').attr('checked',false);
                                    $('input[name=q11]').attr('checked',false);
                                    $('input[name=q12]').attr('checked',false);
                                    $('input[name=q13]').attr('checked',false);
                                    $('input[name=q14]').attr('checked',false);
                                    $('input[name=q15]').attr('checked',false);





                                    },
                         error : function (error){
                                    console.log(error);
                                    }


                          });
               });

            });
