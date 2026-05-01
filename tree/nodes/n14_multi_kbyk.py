# tree/nodes/n14_multi_kbyk.py

from utils.images import get_image_base64, IMG_BASE_PATH

_img_single = get_image_base64(f"{IMG_BASE_PATH}G13kClass_1Label_figC.jpg")
_img_table1 = get_image_base64(f"{IMG_BASE_PATH}G15kClass_ordinal_ConfusionTab_figC.jpg")
_img_table2 = get_image_base64(f"{IMG_BASE_PATH}G14kClass_ordinal_ConfusionTab_eg_figC.jpg")

def _img_tag(img_b64, alt):
    if img_b64:
        return (f'<div style="text-align:center;margin:1.5rem 0;">'
                f'<img src="data:image/jpeg;base64,{img_b64}" alt="{alt}" '
                f'style="max-width:100%;height:auto;border:1px solid #ddd;'
                f'border-radius:4px;padding:5px;"></div>')
    return '<p style="color:#999;font-style:italic;">[Image not available]</p>'

_OVERVIEW = f"""
  <section style="margin-bottom: 1.5rem;">
   <h2 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 0.5rem; color: #1a202c;">Overview</h2>
   <p style="color: #333; line-height: 1.6;">Based on your answers, your task is a <i>multi-class nominal classification</i> task, based on a <i>reference standard with negligible variability</i>, and returns a single label output for each input (see the figure below for an example output). The evaluation metrics used for this type of classification task are typically based on a <i>k</i>x<i>k</i> confusion matrix. You may choose a metric from the list at the bottom to learn more about it. Before proceeding, it may be helpful to familiarize yourself with the following notation, which may be used in the subsequent nodes.</p>
  </section>
  <section style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Notations used in nodes below</h3>
   <p style="color: #333; line-height: 1.6;">For the <i>i</i><sup style="font-size: 0.7em;">th</sup> case/observation, the output of the <i>k</i>-class classifier in this branch is denoted by &#375;<sub style="font-size: 0.75em;">i</sub> that represents the single class label predicted by the classifier for the observation, as shown in the figure below.</p>
  </section>
  {_img_tag(_img_single, "Figure: example output - single class label")}
  <p style="color: #666; margin-top: 1rem; font-style: italic; text-align: center;">Figure: example output - single class label (most likely class) for the <i>i</i><sup style="font-size: 0.7em;">th</sup> case</p>
"""

_BALANCED_ACC = f"""
  <section style="margin-bottom: 1.5rem;">
   <h2 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 0.5rem; color: #1a202c;">Balanced Accuracy</h2>
   <p style="color: #333; line-height: 1.6;">In a <i>binary</i> classification setting,</p>
   <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
    <li>Sensitivity is the fraction of correctly classified positive cases, i.e., the probability that the AI/ML output is positive when the individual (or case, image, region of interest) is positive based on the reference standard.</li>
    <li>Specificity is the fraction of correctly classified negative cases, i.e., the probability that the AI/ML output is negative when the individual (or case, image, region of interest) is negative based on the reference standard.</li>
   </ul>
   <p style="color: #333; line-height: 1.6;">For a <i>k</i>-class classification problem,</p>
   <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
    <li>Class-specific accuracy for class <i>i</i> is the probability of AI/ML assigning an individual (or case, image, region of interest) to class <i>i</i> given that the individual belongs to class <i>i</i> (<i>i</i> = 1,2,...,<i>k</i>).</li>
    <li>Balanced accuracy is the average (specifically, the arithmetic mean) of the class-specific accuracies over all classes.</li>
   </ul>
   <p style="color: #333; line-height: 1.6;">In the <i>binary</i> classification setting, balanced accuracy is the average of sensitivity and specificity.</p>
  </section>
  <section style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Mathematical formulation</h3>
   <p style="color: #333; line-height: 1.6;">Table 1. Confusion Matrix for <i>k</i>-class classification problem</p>
   {_img_tag(_img_table1, "Table 1: Confusion Matrix for k-class classification")}
   <p style="color: #333; line-height: 1.6;">Every case in the cohort should be assigned to one and only one of the <i>k</i> classes, (e.g., in a respiratory disease multi-class algorithm, each case should be assigned to one class, and if normal cases are included in the cohort, then there should also be a normal class).</p>
   <p style="color: #333; line-height: 1.6;">Revisiting the <i>k</i>-class confusion matrix as shown earlier, class-specific accuracy for class <i>i</i> is defined as:</p>
   <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
    <span style="font-size: 1.05rem; line-height: 2;">
     Class-specific accuracy for class <i>i</i> = <i>n</i><sub style="font-size: 0.7em;">ii</sub> / <i>n</i><sub style="font-size: 0.7em;">+i</sub>
    </span>
   </p>
   <p style="color: #333; line-height: 1.6;">Balanced accuracy is then defined as:</p>
   <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
    <span style="font-size: 1.05rem; line-height: 2;">
     Balanced accuracy = (1/<i>k</i>) <span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em; vertical-align: sub; margin-left: -0.3rem;"><i>i</i>=1</sub><sup style="font-size: 0.65em; vertical-align: super; margin-left: -0.5rem;"><i>k</i></sup> (<i>n</i><sub style="font-size: 0.7em;">ii</sub> / <i>n</i><sub style="font-size: 0.7em;">+i</sub>)
    </span>
   </p>
  </section>
  <section style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Notes and Resources</h3>
   <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
    <li>Balanced accuracy (Carrillo et al., 2014) may have varying names in different literature. For example, 'macro average arithmetic (MAvA)' in Ferri et al. (2009) and 'macro average recall' in Pathan (2021) are both defined the same way as balanced accuracy.</li>
    <li>Carrillo et al. (2014) describes a method to perform a probabilistic evaluation (including the 95% credible intervals) of balanced accuracy for a multi-class problem based on a Bayesian approach. The MATLAB software for the method is available at <a href="https://mloss.org/software/view/447/" target="_blank" style="color: #2b6cb0; text-decoration: underline;">https://mloss.org/software/view/447/</a>.</li>
    <li>Note that balanced accuracy is different from the measure, overall accuracy, which can be affected by disease prevalence. Overall Accuracy is defined as:
     <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
      <span style="font-size: 1.05rem; line-height: 2;">
       Overall accuracy = (1/<i>N</i>) <span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em; vertical-align: sub; margin-left: -0.3rem;"><i>i</i>=1</sub><sup style="font-size: 0.65em; vertical-align: super; margin-left: -0.5rem;"><i>k</i></sup> <i>n</i><sub style="font-size: 0.7em;">ii</sub>
      </span>
     </p>
    </li>
    <li>Summarizing all the results with a single number is convenient, but not always the best strategy. Instead of using balanced accuracy as a metric alone, it is more informative to provide each class-specific accuracy as well as the balanced accuracy.</li>
   </ul>
  </section>
  <section style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Example</h3>
   <p style="color: #333; line-height: 1.6;">Table 2. Confusion Matrix</p>
   {_img_tag(_img_table2, "Table 2: Confusion Matrix Example")}
   <p style="color: #333; line-height: 1.6;">Revisiting the example confusion matrix as shown earlier</p>
   <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
    <li>Class-specific accuracy for class <i>i</i> = 1, 2, 3 respectively
     <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
      <span style="font-size: 1.05rem; line-height: 2;">
       Acc(1) = 95/100 = 0.95<br>
       Acc(2) = 35/50 = 0.7<br>
       Acc(3) = 120/200 = 0.6
      </span>
     </p>
    </li>
    <li>Balanced Accuracy is therefore equal to (0.95+0.7+0.6)/3 = 0.75.</li>
   </ul>
   <p style="color: #333; line-height: 1.6;">Applying the aforementioned Matlab package by Carrillo et al. (2014), one can obtain a 95% credible interval for balanced accuracy in this example (0.69, 0.79).</p>
   <p style="color: #333; line-height: 1.6;">Note that balanced accuracy is different from <i>overall accuracy</i>, which is
    <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
     <span style="font-size: 1.05rem; line-height: 2;">
      Overall accuracy = (95+35+120)/350 = 0.71
     </span>
    </p>
   </p>
  </section>
  <section style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">References</h3>
   <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
    <li>Carrillo, H., Broderson, K.H., Castellanos, J.A. (2014). Probabilistic performance evaluation for multiclass classification using the posterior balanced accuracy. In ROBOT2013: First Iberian Robotics Conference (pp. 347-361). Springer, Cham.</li>
    <li>Ferri, C., Hernandez-Orallo, J., &amp; Modroiu, R. (2009). An experimental comparison of performance measures for classification. Pattern Recognition Letters, 30(1), 27-38.</li>
    <li>Pathan, A.S.K. (Ed.). (2021). Securing Social Networks in Cyberspace. CRC Press.</li>
   </ul>
  </section>
"""

_MACRO_PREC_REC = f"""
  <section style="margin-bottom: 1.5rem;">
   <h2 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 0.5rem; color: #1a202c;">(Macro average precision, macro average recall) pair</h2>
   <p style="color: #333; line-height: 1.6;">In a <i>binary</i> classification setting,</p>
   <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
    <li>Precision (= positive predictive value, or PPV), is the probability that the individual (or case, image, region of interest) is positive based on the reference standard when the AI/ML output is positive.</li>
    <li>Recall (= sensitivity) is the probability that the AI/ML output is positive when the individual (or case, image, region of interest) is positive based on the reference standard.</li>
   </ul>
  </section>
  <section style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Definitions for a <i>k</i>-class classification problem</h3>
   <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
    <li>Class-specific precision for class <i>i</i> is the probability that an individual (or case, image, region of interest) belongs to class <i>i</i> given that the individual is assigned to class <i>i</i> (<i>i</i> = 1,2,...,<i>k</i>) by the AI/ML output.</li>
    <li>Class-specific recall for class <i>i</i> is the probability that AI/ML assigns an individual (or case, image, region of interest) to class <i>i</i> given that the individual belongs to class <i>i</i> (<i>i</i> = 1,2,...,<i>k</i>).</li>
    <li>Macro average precision (Pathan, 2021) is the average (specifically, the arithmetic mean) of the class-specific precision over all classes.</li>
    <li>Macro average recall (Pathan, 2021) is the average (specifically, the arithmetic mean) of the class-specific recall over all classes.</li>
   </ul>
  </section>
  <section style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Mathematical Formulation</h3>
   <p style="color: #333; line-height: 1.6;">Table 1. Confusion Matrix for <i>k</i>-class classification problem</p>
   {_img_tag(_img_table1, "Table 1: Confusion Matrix for k-class classification")}
   <p style="color: #333; line-height: 1.6;">Every case in the cohort should be assigned to one and only one of the <i>k</i> classes, (e.g., in a respiratory disease multi-class algorithm, each case should be assigned to one class, and if normal cases are included in the cohort, then there should also be a normal class).</p>
   <p style="color: #333; line-height: 1.6;">Revisiting the <i>k</i>-class confusion matrix as shown in Table 1 earlier, class-specific precision and recall for class <i>i</i> are respectively defined as</p>
   <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
    <span style="font-size: 1.05rem; line-height: 2;">
     precision(class <i>i</i>) = <i>n</i><sub style="font-size: 0.7em;">ii</sub> / <i>n</i><sub style="font-size: 0.7em;">i+</sub><br><br>
     recall(class <i>i</i>) = <i>n</i><sub style="font-size: 0.7em;">ii</sub> / <i>n</i><sub style="font-size: 0.7em;">+i</sub>
    </span>
   </p>
   <p style="color: #333; line-height: 1.6;">Macro average precision and recall are then defined respectively as</p>
   <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
    <span style="font-size: 1.05rem; line-height: 2;">
     Macro average precision = (1/<i>k</i>) <span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em; vertical-align: sub; margin-left: -0.3rem;"><i>i</i>=1</sub><sup style="font-size: 0.65em; vertical-align: super; margin-left: -0.5rem;"><i>k</i></sup> (<i>n</i><sub style="font-size: 0.7em;">ii</sub> / <i>n</i><sub style="font-size: 0.7em;">i+</sub>)<br><br>
     Macro average recall = (1/<i>k</i>) <span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em; vertical-align: sub; margin-left: -0.3rem;"><i>i</i>=1</sub><sup style="font-size: 0.65em; vertical-align: super; margin-left: -0.5rem;"><i>k</i></sup> (<i>n</i><sub style="font-size: 0.7em;">ii</sub> / <i>n</i><sub style="font-size: 0.7em;">+i</sub>)
    </span>
   </p>
  </section>
  <section style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Notes and Resources</h3>
   <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
    <li>Macro average recall is equivalent to balanced accuracy (Carrillo et al., 2014).</li>
    <li>Carrillo et al. (2014) describes a method to perform a probabilistic evaluation (including the 95% credible intervals) of balanced accuracy (i.e., macro average recall) for a multi-class problem based on a Bayesian approach. The MATLAB software for the method is available at <a href="https://mloss.org/software/view/447/" target="_blank" style="color: #2b6cb0; text-decoration: underline;">https://mloss.org/software/view/447/</a>.</li>
    <li>Summarizing all the results with a single number is convenient, but not always the best strategy.</li>
   </ul>
  </section>
  <section style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Example</h3>
   <p style="color: #333; line-height: 1.6;">Table 2. Confusion Matrix</p>
   {_img_tag(_img_table2, "Table 2: Confusion Matrix Example")}
   <p style="color: #333; line-height: 1.6;">Revisiting the example confusion matrix as shown earlier, based on the definition above</p>
   <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
    <li>Class-specific precision and recall for class <i>i</i> = 1, 2, 3, are respectively
     <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
      <span style="font-size: 1.05rem; line-height: 2;">
       Precision<sub style="font-size: 0.7em;">1</sub> = 95/150 = 0.63, Recall<sub style="font-size: 0.7em;">1</sub> = 95/100 = 0.95<br>
       Precision<sub style="font-size: 0.7em;">2</sub> = 35/70 = 0.5, Recall<sub style="font-size: 0.7em;">2</sub> = 35/50 = 0.7<br>
       Precision<sub style="font-size: 0.7em;">3</sub> = 120/130 = 0.92, Recall<sub style="font-size: 0.7em;">3</sub> = 120/200 = 0.6
      </span>
     </p>
    </li>
    <li>Macro average precision and recall can then be computed as
     <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
      <span style="font-size: 1.05rem; line-height: 2;">
       Macro average precision = (0.63+0.50+0.92)/3 = 0.68<br>
       Macro average recall = (0.95+0.7+0.6)/3 = 0.75
      </span>
     </p>
    </li>
   </ul>
  </section>
  <section style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">References</h3>
   <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
    <li>Pathan, A.S.K. (Ed.). (2021). Securing Social Networks in Cyberspace. CRC Press.</li>
    <li>Carrillo, H., Brodersen, K.H., Castellanos, J.A. (2014). Probabilistic performance evaluation for multiclass classification using the posterior balanced accuracy. In ROBOT2013: First Iberian Robotics Conference (pp. 347-361). Springer, Cham.</li>
   </ul>
  </section>
"""

_F1_MULTI = f"""
  <section style="margin-bottom: 1.5rem;">
   <h2 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 0.5rem; color: #1a202c;">F1 score</h2>
   <p style="color: #333; line-height: 1.6;">In a <i>binary</i> classification setting, F1 score is defined as the harmonic mean of precision (PPV) and recall (sensitivity).</p>
   <p style="color: #333; line-height: 1.6;">For a <i>k</i>-class classification problem,</p>
   <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
    <li>Class-specific F1 score for class <i>i</i> is the harmonic mean of class-specific precision (PPV) and class-specific recall (sensitivity) for class <i>i</i>.</li>
    <li>Macro F1 score (Opitz &amp; Burst, 2019) is the average (specifically, the arithmetic mean) of the class-specific F1 scores over all classes.</li>
   </ul>
  </section>
  <section style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Mathematical formulation</h3>
   <p style="color: #333; line-height: 1.6;">Table 1. Confusion matrix for <i>k</i>-class classification problem</p>
   {_img_tag(_img_table1, "Table 1: Confusion Matrix for k-class classification")}
   <p style="color: #333; line-height: 1.6;">Every case in the cohort should be assigned to one and only one of the <i>k</i> classes.</p>
   <p style="color: #333; line-height: 1.6;">Revisiting the <i>k</i>-class confusion matrix as shown in Table 1, class-specific F1 score for class <i>i</i> is defined as</p>
   <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
    <span style="font-size: 1.05rem; line-height: 2;">
     F1(<i>i</i>) = 2 &#183; (Precision(<i>i</i>) &#183; Recall(<i>i</i>)) / (Precision(<i>i</i>) + Recall(<i>i</i>))
    </span>
   </p>
   <p style="color: #333; line-height: 1.6;">Macro F1 is then defined as</p>
   <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
    <span style="font-size: 1.05rem; line-height: 2;">
     Macro F1 = (1/<i>k</i>) <span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em; vertical-align: sub; margin-left: -0.3rem;"><i>i</i>=1</sub><sup style="font-size: 0.65em; vertical-align: super; margin-left: -0.5rem;"><i>k</i></sup> F1(<i>i</i>)
    </span>
   </p>
  </section>
  <section style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Notes and Resources</h3>
   <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
    <li>Macro F1 may have different defining formulas in different literature. Displayed is the first definition, 'averaged F1', which is found to be more robust compared to the other definition, and thus is recommended by Opitz &amp; Burst (2019).</li>
    <li>Takahashi et al. (2021) describes methods to estimate F1 scores with confidence intervals based on the large sample multivariate central limit theorem. The R code is given as Appendix D in their article.</li>
    <li>Note, that macro F1 is different from micro F1 (for definition see Takahashi et al., 2021). Micro F1 is known to be equivalent to overall accuracy (Panigrahi et al., 2021).</li>
   </ul>
  </section>
  <section style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Examples</h3>
   <p style="color: #333; line-height: 1.6;">Table 2. Confusion Matrix: Example</p>
   {_img_tag(_img_table2, "Table 2: Confusion Matrix Example")}
   <p style="color: #333; line-height: 1.6;">Using the confusion matrix as shown in Table 2, based on the definition above</p>
   <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
    <li>Class-specific F1 score for class <i>i</i> = 1, 2, 3 is respectively
     <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
      <span style="font-size: 1.05rem; line-height: 2;">
       F1<sub style="font-size: 0.7em;">1</sub> = 2&#183;(0.63&#183;0.95)/(0.63+0.95) = 0.76<br>
       F1<sub style="font-size: 0.7em;">2</sub> = 2&#183;(0.5&#183;0.7)/(0.5+0.7) = 0.58<br>
       F1<sub style="font-size: 0.7em;">3</sub> = 2&#183;(0.92&#183;0.6)/(0.92+0.6) = 0.73
      </span>
     </p>
    </li>
    <li>Macro F1 is then computed as
     <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
      <span style="font-size: 1.05rem; line-height: 2;">
       Macro F1 = (0.76+0.58+0.73)/3 = 0.69
      </span>
     </p>
    </li>
   </ul>
  </section>
  <section style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">References</h3>
   <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
    <li>Opitz, J., &amp; Burst, S. (2019). MacroF1 and macro F1.</li>
    <li>Takahashi, K., Yamamoto, K., Kuchiba, A., &amp; Koyama, T. (2021). Confidence interval for micro-averaged F1 and macro-averaged F1 scores. Applied Intelligence, 1-12.</li>
    <li>Panigrahi, C. R., Pati, B., Rath, M., &amp; Buyya, R. (Eds.). (2021). Computational Modeling and Data Analysis in COVID-19 Research. CRC Press.</li>
   </ul>
  </section>
"""

_MCC_MULTI = f"""
  <section style="margin-bottom: 1.5rem;">
   <h2 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 0.5rem; color: #1a202c;">Matthews Correlation Coefficient (MCC)</h2>
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Background</h3>
   <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
    <li>Matthews Correlation Coefficient (MCC) was originally introduced by biochemist Brian W. Matthews in 1975 (Matthews, 1975) as a measure of the quality of binary classification problems.</li>
    <li>MCC is generally regarded as a balanced measure which can be used in <i>binary</i> classification even if the sizes of classes are very different (Chicco &amp; Jurman, 2020).</li>
    <li>Later, MCC was extended by Gorodkin (2004) to multi-class classification problems. The mathematical definition is given below.</li>
   </ul>
  </section>
  <section style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Mathematical Formulation</h3>
   <p style="color: #333; line-height: 1.6;">Table 1. Confusion Matrix for <i>k</i>-class classification problem</p>
   {_img_tag(_img_table1, "Table 1: Confusion Matrix for k-class classification")}
   <p style="color: #333; line-height: 1.6;">Every case in the cohort should be assigned to one and only one of the <i>k</i> classes.</p>
   <p style="color: #333; line-height: 1.6;">Revisiting the <i>k</i>-class confusion matrix as shown in Table 1, MCC for a <i>k</i>-class classification problem is defined as (Rocha et al., 2021)</p>
   <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
    <span style="font-size: 1.05rem; line-height: 2;">
     MCC = [<i>N</i> <span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em;"><i>i</i>=1</sub><sup style="font-size: 0.65em;"><i>k</i></sup> <i>n</i><sub style="font-size: 0.7em;">ii</sub> &#8722; <span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em;"><i>i</i>=1</sub><sup style="font-size: 0.65em;"><i>k</i></sup> <i>n</i><sub style="font-size: 0.7em;">i+</sub> <i>n</i><sub style="font-size: 0.7em;">+i</sub>] / &#8730;[(<i>N</i>&#178; &#8722; <span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em;"><i>i</i>=1</sub><sup style="font-size: 0.65em;"><i>k</i></sup> <i>n</i><sub style="font-size: 0.7em;">i+</sub>&#178;)(<i>N</i>&#178; &#8722; <span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em;"><i>i</i>=1</sub><sup style="font-size: 0.65em;"><i>k</i></sup> <i>n</i><sub style="font-size: 0.7em;">+i</sub>&#178;)]
    </span>
   </p>
  </section>
  <section style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Notes and Resources</h3>
   <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
    <li>The range of MCC is [&#8722;1, 1].</li>
    <li>The Python function "sklearn.metrics.matthews_corrcoef" can be used to compute the estimate of MCC.</li>
   </ul>
  </section>
  <section style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Example</h3>
   <p style="color: #333; line-height: 1.6;">Table 2. Confusion Matrix: Example</p>
   {_img_tag(_img_table2, "Table 2: Confusion Matrix Example")}
   <p style="color: #333; line-height: 1.6;">As per the example confusion matrix as shown in Table 2, based on the definition above, MCC is</p>
   <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
    <span style="font-size: 1.05rem; line-height: 2;">
     MCC = [350&#183;(95+35+120) &#8722; (150&#183;100 + 70&#183;50 + 130&#183;200)] / &#8730;[(350&#178; &#8722; 150&#178; &#8722; 70&#178; &#8722; 130&#178;)(350&#178; &#8722; 100&#178; &#8722; 50&#178; &#8722; 200&#178;)] = 0.5812
    </span>
   </p>
  </section>
  <section style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">References</h3>
   <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
    <li>Matthews, B. W. (1975). Comparison of the predicted and observed secondary structure of T4 phage lysozyme. Biochimica et Biophysica Acta (BBA)-Protein Structure, 405(2), 442-451.</li>
    <li>Chicco, D., &amp; Jurman, G. (2020). The advantages of the Matthews correlation coefficient (MCC) over F1 score and accuracy in binary classification evaluation. BMC genomics, 21(1), 1-13.</li>
    <li>Gorodkin J (2004) Comparing two K-category assignments by a K-category correlation coefficient. Computational Biology and Chemistry 28: 367-374.</li>
    <li>Rocha, M., Fdez-Riverola, F., Mohamad, M. S., &amp; Casado-Vara, R. (Eds.). (2021). Practical Applications of Computational Biology &amp; Bioinformatics, 15th International Conference (PACBB 2021) (Vol. 325, Page 14). Springer Nature.</li>
   </ul>
  </section>
"""

_KAPPA_MULTI = f"""
  <section style="margin-bottom: 1.5rem;">
   <h2 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 0.5rem; color: #1a202c;">Cohen's Kappa</h2>
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Background</h3>
   <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
    <li>Cohen's Kappa was originally proposed by Cohen in 1960 (Cohen, 1960) in order to measure the agreement between two raters for categorical items, by taking into account the possibility of the agreement occurring by chance.</li>
    <li>The original defining formula of Cohen's Kappa is as follows
     <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
      <span style="font-size: 1.05rem; line-height: 2;">
       &#954; = (p<sub style="font-size: 0.7em;">o</sub> &#8722; p<sub style="font-size: 0.7em;">e</sub>) / (1 &#8722; p<sub style="font-size: 0.7em;">e</sub>)
      </span>
     </p>
     <p style="color: #333; line-height: 1.6;">where p<sub style="font-size: 0.75em;">o</sub> is the relative <i>observed</i> agreement among raters, p<sub style="font-size: 0.75em;">e</sub> is the <i>hypothetical</i> probability of chance agreement.</p>
    </li>
    <li>Later, Cohen's Kappa was also used by other literature, per Aggarwal &amp; Charu (2014) below, as a performance metric for <i>binary</i> and <i>multi-class</i> classification problem.</li>
   </ul>
  </section>
  <section style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Mathematical formulation</h3>
   <p style="color: #333; line-height: 1.6;">Every case in the cohort should be assigned to one and only one of the <i>k</i> classes.</p>
   <p style="color: #333; line-height: 1.6;">As per the <i>k</i>-class confusion matrix as shown earlier, Cohen's Kappa for a <i>k</i>-class classification problem is defined as (Aggarwal &amp; Charu, 2014)</p>
   <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
    <span style="font-size: 1.05rem; line-height: 2;">
     &#954; = [<i>N</i> <span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em;"><i>i</i>=1</sub><sup style="font-size: 0.65em;"><i>k</i></sup> <i>n</i><sub style="font-size: 0.7em;">ii</sub> &#8722; <span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em;"><i>i</i>=1</sub><sup style="font-size: 0.65em;"><i>k</i></sup> <i>n</i><sub style="font-size: 0.7em;">i+</sub> <i>n</i><sub style="font-size: 0.7em;">+i</sub>] / [<i>N</i>&#178; &#8722; <span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em;"><i>i</i>=1</sub><sup style="font-size: 0.65em;"><i>k</i></sup> <i>n</i><sub style="font-size: 0.7em;">i+</sub> <i>n</i><sub style="font-size: 0.7em;">+i</sub>]
    </span>
   </p>
  </section>
  <section style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Notes and Resources</h3>
   <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
    <li>Cohen's Kappa is generally thought to be a more robust measure than simple percent agreement calculation, as Kappa takes into account the possibility of the agreement occurring by chance.</li>
    <li>The range of Cohen's Kappa is [&#8722;1, 1].</li>
    <li>Note, that there are different versions of interpretation for the degree of agreement based on Kappa's value, for example, Cohen (1960) and McHugh (2012).</li>
    <li>R package "psych" (<a href="https://www.rdocumentation.org/packages/psych/versions/2.1.9/topics/cohen.kappa" target="_blank" style="color: #2b6cb0; text-decoration: underline;">https://www.rdocumentation.org/packages/psych/versions/2.1.9/topics/cohen.kappa</a>) provides functions to compute point estimate and confidence interval for Cohen's Kappa.</li>
    <li>R package 'irr' (<a href="https://cran.r-project.org/web/packages/irr/irr.pdf" target="_blank" style="color: #2b6cb0; text-decoration: underline;">https://cran.r-project.org/web/packages/irr/irr.pdf</a>) also provides functions to compute estimate for Cohen's Kappa.</li>
   </ul>
  </section>
  <section style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Example</h3>
   <p style="color: #333; line-height: 1.6;">Table 2. Confusion Matrix: Example</p>
   {_img_tag(_img_table2, "Table 2: Confusion Matrix Example")}
   <p style="color: #333; line-height: 1.6;">As per the confusion matrix in Table 2, based on the definition above, Cohen's Kappa is</p>
   <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
    <span style="font-size: 1.05rem; line-height: 2;">
     &#954; = [350&#183;(95+35+120) &#8722; (150&#183;100 + 70&#183;50 + 130&#183;200)] / [350&#178; &#8722; (150&#183;100 + 70&#183;50 + 130&#183;200)] = 0.55
    </span>
   </p>
   <p style="color: #333; line-height: 1.6;">The obtained Cohen's Kappa is 0.55, which suggests there is weak or moderate agreement between the classifier and the ground truth.</p>
  </section>
  <section style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">References</h3>
   <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
    <li>Cohen, Jacob (1960). "A coefficient of agreement for nominal scales". Educational and Psychological Measurement. 20 (1): 37-46.</li>
    <li>Aggarwal, C. C., &amp; Charu, C. Data Classification: Algorithms and Applications; 2014. (Page 638). Taylor &amp; Francis.</li>
    <li>Guggenmoos-Holzmann, I. (1996). The meaning of kappa: probabilistic concepts of reliability and validity revisited. Journal of clinical epidemiology, 49(7), 775-782.</li>
    <li>McHugh, M. L. (2012). Interrater reliability: the kappa statistic. Biochemia medica, 22(3), 276-282.</li>
    <li>Fleiss, J. L., Cohen, J., &amp; Everitt, B. S. (1969). Large sample standard errors of kappa and weighted kappa. Psychological bulletin, 72(5), 323.</li>
    <li>Cohen, J. (1968). Weighted kappa: nominal scale agreement provision for scaled disagreement or partial credit. Psychological bulletin, 70(4), 213.</li>
   </ul>
  </section>
"""

_NMI_MULTI = f"""
  <section style="margin-bottom: 1.5rem;">
   <h2 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 0.5rem; color: #1a202c;">Normalized Mutual Information</h2>
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Background</h3>
   <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
    <li>In information theory, the <i>mutual information</i> of two random variables is a measure of the dependency between two variables, as originally defined by Shannon (1948) and Fano (Kreer, 1957).</li>
    <li>The concept of mutual information is closely related to that of <i>entropy</i> of a random variable, which is an information theory-based measure to quantify the amount of information in a random variable, and that of <i>joint entropy</i>, which measures the uncertainty associated with a set of variables.</li>
    <li>Given a discrete variable <i>x</i>, the <i>entropy</i> of <i>x</i> is defined as
     <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
      <span style="font-size: 1.05rem; line-height: 2;">
       <i>H</i>(<i>x</i>) = &#8722; <span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em;"><i>x</i>&#8712;<i>X</i></sub> <i>p</i>(<i>x</i>) log <i>p</i>(<i>x</i>)
      </span>
     </p>
    </li>
    <li>Given two discrete variables <i>x</i> and <i>y</i>, the <i>joint entropy</i> between <i>x</i> and <i>y</i> is defined as
     <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
      <span style="font-size: 1.05rem; line-height: 2;">
       <i>H</i>(<i>x</i>,<i>y</i>) = &#8722; <span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em;"><i>x</i>&#8712;<i>X</i></sub> <span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em;"><i>y</i>&#8712;<i>Y</i></sub> <i>p</i>(<i>x</i>,<i>y</i>) log <i>p</i>(<i>x</i>,<i>y</i>)
      </span>
     </p>
    </li>
    <li>The <i>mutual information</i> between <i>x</i> and <i>y</i> is defined as
     <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
      <span style="font-size: 1.05rem; line-height: 2;">
       <i>I</i>(<i>x</i>,<i>y</i>) = <i>H</i>(<i>x</i>) &#8722; <i>H</i>(<i>x</i>&#124;<i>y</i>)
      </span>
     </p>
     <p style="color: #333; line-height: 1.6;">where <i>H</i>(<i>x</i>&#124;<i>y</i>) is the conditional entropy, which can be interpreted as the amount of information needed to describe the outcome of the random variable <i>x</i> given that the value of another random variable, <i>y</i>, is known.</p>
    </li>
    <li>To apply <i>mutual information</i> to a classification problem, we interpret <i>x</i> as the <i>true</i> class label and x&#x0302; as the <i>predicted</i> class label.</li>
    <li style="list-style-type: none; margin-left: -1.5rem;">Note that <i>I</i>(<i>x</i>, x&#x0302;) varies between 0 and <i>H</i>(<i>x</i>):
     <div style="margin-left: 1.5rem; margin-top: 0.5rem;">
      <p style="color: #333; line-height: 1.6; margin-bottom: 0.5rem;">
       &#183; If the predicted labels do not provide any information about the true labels, then
       <i>H</i>(<i>x</i>&#124;x&#x0302;) = <i>H</i>(<i>x</i>) (the amount of information needed to describe <i>x</i>
       after observing x&#x0302; is still <i>H</i>(<i>x</i>)), and thus <i>I</i>(<i>x</i>, x&#x0302;) = 0.
      </p>
      <p style="color: #333; line-height: 1.6;">
       &#183; If the predicted labels provide perfect information about the true labels, then
       <i>H</i>(<i>x</i>&#124;x&#x0302;) = 0 (the amount of information needed to describe <i>x</i>
       after observing x&#x0302; is 0), and thus <i>I</i>(<i>x</i>, x&#x0302;) = <i>H</i>(<i>x</i>).
      </p>
     </div>
    </li>
    <li>To provide a metric that is independent of the entropy of the true labels, mutual information is therefore normalized with <i>H</i>(<i>x</i>), yielding a metric value between 0 and 1. The metric is named as <b>normalized mutual information</b> (Baldi et al., 2000), and defined as the following:
     <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
      <span style="font-size: 1.05rem; line-height: 2;">
       NMI = <i>I</i>(<i>x</i>, x&#x0302;) / <i>H</i>(<i>x</i>) = (<i>H</i>(<i>x</i>) + <i>H</i>(x&#x0302;) &#8722; <i>H</i>(<i>x</i>, x&#x0302;)) / <i>H</i>(<i>x</i>)
      </span>
     </p>
    </li>
   </ul>
  </section>
  <section style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Mathematical formulation</h3>
   <p style="color: #333; line-height: 1.6;">Table 1. Confusion Matrix for <i>k</i>-class classification problem</p>
   {_img_tag(_img_table1, "Table 1: Confusion Matrix for k-class classification")}
   <p style="color: #333; line-height: 1.6;">Every case in the cohort should be assigned to one and only one of the <i>k</i> classes, (e.g., in a respiratory disease multi-class algorithm, each case should be assigned to one class, and if normal cases are included in the cohort, then there should also be a normal class).</p>
   <p style="color: #333; line-height: 1.6;">As per the <i>k</i>-class confusion matrix shown in Table 1 earlier, <i>normalized mutual information</i> for a <i>k</i>-class classification problem can be expressed as below (Baldi et al., 2000)</p>
   <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
    <span style="font-size: 1.05rem; line-height: 2.2;">
     NMI = [&#8722;<span style="font-size: 1.2rem;">&#8721;</span><sub style="font-size: 0.65em;"><i>i</i>=1</sub><sup style="font-size: 0.65em;"><i>k</i></sup> (<i>n</i><sub>+<i>i</i></sub>/<i>N</i>) log(<i>n</i><sub>+<i>i</i></sub>/<i>N</i>) &#8722; <span style="font-size: 1.2rem;">&#8721;</span><sub style="font-size: 0.65em;"><i>i</i>=1</sub><sup style="font-size: 0.65em;"><i>k</i></sup> (<i>n</i><sub><i>i</i>+</sub>/<i>N</i>) log(<i>n</i><sub><i>i</i>+</sub>/<i>N</i>) + <span style="font-size: 1.2rem;">&#8721;</span><sub style="font-size: 0.65em;"><i>i</i>=1</sub><sup style="font-size: 0.65em;"><i>k</i></sup> <span style="font-size: 1.2rem;">&#8721;</span><sub style="font-size: 0.65em;"><i>j</i>=1</sub><sup style="font-size: 0.65em;"><i>k</i></sup> (<i>n</i><sub><i>ij</i></sub>/<i>N</i>) log(<i>n</i><sub><i>ij</i></sub>/<i>N</i>)]<br>
     / [&#8722;<span style="font-size: 1.2rem;">&#8721;</span><sub style="font-size: 0.65em;"><i>i</i>=1</sub><sup style="font-size: 0.65em;"><i>k</i></sup> (<i>n</i><sub>+<i>i</i></sub>/<i>N</i>) log(<i>n</i><sub>+<i>i</i></sub>/<i>N</i>)]
    </span>
   </p>
  </section>
  <section style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Example</h3>
   <p style="color: #333; line-height: 1.6;">Table 2. Example: confusion matrix</p>
   {_img_tag(_img_table2, "Table 2: Confusion Matrix Example")}
   <p style="color: #333; line-height: 1.6;">Revisiting the example confusion matrix as shown in Table 2, based on the definition above, we have entropies computed as below</p>
   <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
    <li><i>H</i>(<i>x</i>) = &#8722;<span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em;"><i>i</i>=1</sub><sup style="font-size: 0.65em;"><i>k</i></sup> <i>p</i>(<i>x</i> = <i>i</i>) log <i>p</i>(<i>x</i> = <i>i</i>) = &#8722;<span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em;"><i>i</i>=1</sub><sup style="font-size: 0.65em;"><i>k</i></sup> (<i>n</i><sub style="font-size: 0.7em;">+i</sub>/<i>N</i>) log (<i>n</i><sub style="font-size: 0.7em;">+i</sub>/<i>N</i>) = &#8722;((100/350) &#183; log(100/350) + (50/350) &#183; log(50/350) + (200/350) &#183; log(200/350)) = 1.379.</li>
    <li><i>H</i>(x&#x0302;) = &#8722;<span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em;"><i>i</i>=1</sub><sup style="font-size: 0.65em;"><i>k</i></sup> <i>p</i>(x&#x0302; = <i>i</i>) log <i>p</i>(x&#x0302; = <i>i</i>) = &#8722;<span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em;"><i>i</i>=1</sub><sup style="font-size: 0.65em;"><i>k</i></sup> (<i>n</i><sub style="font-size: 0.7em;">i+</sub>/<i>N</i>) log (<i>n</i><sub style="font-size: 0.7em;">i+</sub>/<i>N</i>) = &#8722;((150/350) &#183; log(150/350) + (70/350) &#183; log(70/350) + (130/350) &#183; log(130/350)) = 1.519.</li>
    <li>Joint entropy is <i>H</i>(<i>x</i>, x&#x0302;) = &#8722;<span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em;"><i>i</i>=1</sub><sup style="font-size: 0.65em;"><i>k</i></sup> <span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em;"><i>j</i>=1</sub><sup style="font-size: 0.65em;"><i>k</i></sup> <i>p</i>(<i>x</i> = <i>i</i>, x&#x0302; = <i>j</i>) log <i>p</i>(<i>x</i> = <i>i</i>, x&#x0302; = <i>j</i>) = &#8722;((95/350) &#183; log(95/350) + (5/350) &#183; log(5/350) + (50/350) &#183; log(50/350) + (5/350) &#183; log(5/350) + (35/350) &#183; log(35/350) + (30/350) &#183; log(30/350) + (0/350) &#183; log(0/350) + (10/350) &#183; log(10/350) + (120/350) &#183; log(120/350)) = 2.399</li>
    <li>The <b>mutual information</b> is MI = <i>H</i>(<i>x</i>) + <i>H</i>(x&#x0302;) &#8722; <i>H</i>(<i>x</i>, x&#x0302;) = 1.379 + 1.519 &#8722; 2.399 = 0.499.</li>
    <li>The <b>normalized mutual information</b> is then NMI = (<i>H</i>(<i>x</i>) + <i>H</i>(x&#x0302;) &#8722; <i>H</i>(<i>x</i>, x&#x0302;)) / <i>H</i>(<i>x</i>) = 0.499 / 1.379 = 0.362</li>
   </ul>
  </section>
  <section style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">References</h3>
   <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
    <li>Shannon, C. E. (1948). A mathematical theory of communication. The Bell system technical journal, 27(3), 379-423.</li>
    <li>Kreer, J. (1957). A question of terminology. IRE Transactions on Information Theory, 3(3), 208-208.</li>
    <li>Metz, C. E., Goodenough, D. J., &amp; Rossmann, K. (1973). Evaluation of receiver operating characteristic curve data in terms of information theory, with applications in radiography. Radiology, 109(2), 297-303.</li>
    <li>Baldi, P., Brunak, S., Chauvin, Y., Andersen, C. A., &amp; Nielsen, H. (2000). Assessing the accuracy of prediction algorithms for classification: an overview. Bioinformatics, 16(5), 412-424.</li>
   </ul>
  </section>
"""

NODE = {
    "id": "N1_4",
    "title": "Multi-Class Classification: Metrics based on a kxk confusion matrix",
    "type": "metric_selector",
    "overview_html": _OVERVIEW,
    "metrics": {
        "Balanced accuracy": {
            "html": _BALANCED_ACC, "latex": []},
        "(Macro average precision, macro average recall) pair": {
            "html": _MACRO_PREC_REC, "latex": []},
        "F1 score": {
            "html": _F1_MULTI, "latex": []},
        "Matthews Correlation Coefficient": {
            "html": _MCC_MULTI, "latex": []},
        "Cohen's kappa": {
            "html": _KAPPA_MULTI, "latex": []},
        "Normalized Mutual information": {
            "html": _NMI_MULTI, "latex": []},
    },
}
