#!/usr/bin/env roseus

(load "rcb4robots.l")
(make-kxr-robot "kxrl2l2a6h2m")

(ros::load-ros-manifest "roseus")
(ros::roseus "action_sub")

(print "before com-init")
(send *ri* :com-init)
(print "after com-init before hold")
(send *ri* :hold)
(print "after hold before neutral")
(send *ri* :neutral)
(print "after hold before neutral")

;; callback function
(defun cb (msg)
  (setq action (send msg :data))
  (print "in the action callback function")
  (print action)
  (if (string-equal action 'nod)
	  (progn
		(send *robot* :neutral)
		(send *robot* :head-neck-p :joint-angle 30)
		(send *ri* :angle-vector (send *robot* :angle-vector) 500)
		;; (wait-interpolation)
		(send *robot* :head-neck-p :joint-angle -30)
		(send *ri* :angle-vector (send *robot* :angle-vector) 500)
		;; (wait-interpolation)
		(send *robot* :head-neck-p :joint-angle 30)
		(send *ri* :angle-vector (send *robot* :angle-vector) 500)
		(send *robot* :head-neck-p :joint-angle 0)
		(send *ri* :angle-vector (send *robot* :angle-vector) 500)
		)
    )
  )


(ros::subscribe "action" std_msgs::string #'cb)

(do-until-key
 (ros::spin-once)
)
