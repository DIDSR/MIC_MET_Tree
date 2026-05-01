# tree/nodes/n02_binary_2x2.py

from utils.images import get_image_base64, IMG_BASE_PATH

_img_2x2 = get_image_base64(f"{IMG_BASE_PATH}G02binary2x2_FigC.jpg")
_img_tag = (
    f'<div style="text-align:center;margin:1.5rem 0;">'
    f'<img src="data:image/jpeg;base64,{_img_2x2}" '
    f'alt="2x2 Confusion Matrix" '
    f'style="max-width:100%;height:auto;border:1px solid #ddd;'
    f'border-radius:4px;padding:5px;">'
    f'</div>'
) if _img_2x2 else '<p style="color:#999;font-style:italic;">[Image not available]</p>'

_OVERVIEW = f"""
<section style="margin-bottom: 1.5rem;">
 <h2 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 0.5rem; color: #1a202c;">Overview</h2>
 <p style="color: #333; line-height: 1.6;">Based on your input, your task is a <i>binary</i> classification task, based on a <i>reference standard with negligible variability</i>, and <i>binary AI/ML output</i>. The evaluation metrics used for this type of classification task are typically based on a 2x2 confusion matrix as shown below, where TP, FP, FN, and TN denote the number of true-positive, false-positive, true-negative and false-negative, respectively. You may choose a metric that you are interested in from the list at the bottom to learn more about it.</p>
</section>
{_img_tag}
<section>
 <h3 style="font-size: 1.25rem; font-weight: 600; margin-top: 1.5rem; margin-bottom: 0.75rem; color: #1a202c;">Binary Classification: Metrics based on a 2x2 confusion matrix</h3>
 <p style="color: #666; margin-top: 1rem; font-style: italic;">(Please select a metric from the sidebar to view its details.)</p>
</section>
"""

_SE_SP = """
     <section style="margin-bottom: 1.5rem;">
       <h2 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 0.5rem; color: #1a202c;">Sensitivity and Specificity</h2>
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Definition</h3>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li><b>Sensitivity</b> is the fraction of correctly classified positive cases, meaning the probability that the AI/ML output is positive when the individual (or case, image, region of interest) is positive based on the reference standard.</li>
         <li><b>Specificity</b> is the fraction of correctly classified negative cases, meaning the probability that the AI/ML output is negative when the individual (or case, image, region of interest) is negative based on the reference standard.</li>
         <li>These are based on the following confusion matrix notations:
           <ul style="list-style-type: circle; margin-left: 1.5rem; color: #333;">
             <li><b>TP</b> = true-positive decision</li>
             <li><b>FP</b> = false-positive decision</li>
             <li><b>TN</b> = true-negative decision</li>
             <li><b>FN</b> = false-negative decision</li>
           </ul>
         </li>
       </ul>
     </section>
     <section style="margin-bottom: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Mathematical Formulation</h3>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li>Sensitivity and Specificity are mathematically defined as:
           <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
             <span style="font-size: 1.05rem; line-height: 2;">
               Sensitivity = TP / (TP + FN)
             </span>
           </p>
           <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
             <span style="font-size: 1.05rem; line-height: 2;">
               Specificity = TN / (FP + TN)
             </span>
           </p>
         </li>
       </ul>
     </section>
     <section style="margin-bottom: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Notes and Resources</h3>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li>Zhou et al. (2014) provide point estimates of sensitivity and specificity as well as several approaches for computing their corresponding confidence intervals.</li>
         <li>The `BinomCI` function in the R package "DescTools" (Signorell et al., 2021) can calculate confidence intervals for a binomial proportion (including sensitivity and specificity, which are estimated as sample proportions) using various methods such as "wald", "agresti-coull", "wilson", "jeffreys", etc. Refer to Brown et al. (2001) for a comparison of nine interval estimation methods for a binomial proportion.</li>
         <li>Jovanovic and Levy (1997) discuss a technique for interval estimation when the point estimate is 0 or 1.0.</li>
         <li>Note that the interval estimation methods above assume all observations are independent (i.e., the occurrence of one event or observation does not affect the probability of occurrence of another). This assumption does not hold if, for example, the data includes multiple regions of interest from the same subject. For a discussion of confidence interval estimation for sensitivity and specificity for clustered data, refer to Zhou et al. (2014).</li>
       </ul>
     </section>
     <section style="margin-bottom: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">References</h3>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li>Zhou, X. H., Obuchowski, N. A., &amp; McClish, D. K. (2014). <i>Statistical Methods in Diagnostic Medicine</i>. John Wiley &amp; Sons.</li>
         <li>Signorell, A. et al. (2021). DescTools: Tools for descriptive statistics. R package version 0.99.43.</li>
         <li>Brown, L. D., Cai, T. T., &amp; DasGupta, A. (2001). Interval estimation for a binomial proportion. <i>Statistical science, 16</i>(2), 101-133.</li>
         <li>Jovanovic, B. D., &amp; Levy, P. S. (1997). A look at the rule of three. <i>The American Statistician, 51</i>(2), 137-139.</li>
       </ul>
     </section>
"""

_PRECISION_RECALL = """
     <section style="margin-bottom: 1.5rem;">
       <h2 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 0.5rem; color: #1a202c;">Precision and Recall</h2>
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Definition</h3>
       <p style="color: #333; line-height: 1.6;"><b>Precision</b> (= positive predictive value, or PPV) is the probability that an individual (or case, image, region of interest) is positive based on the reference standard when the AI/ML output is positive.</p>
       <p style="color: #333; line-height: 1.6;"><b>Recall</b> (= sensitivity) is the probability that the AI/ML output is positive when the individual (or case, image, region of interest) is positive based on the reference standard.</p>
       <p style="color: #333; line-height: 1.6;">These are based on the following confusion matrix notations:</p>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li><b>TP</b> = true-positive decision</li>
         <li><b>FP</b> = false-positive decision</li>
         <li><b>TN</b> = true-negative decision</li>
         <li><b>FN</b> = false-negative decision</li>
       </ul>
     </section>
     <section style="margin-bottom: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Mathematical Formulation</h3>
       <p style="color: #333; line-height: 1.6;">Precision and Recall are mathematically defined as:</p>
       <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
         <span style="font-size: 1.05rem; line-height: 2;">
           Recall = sensitivity = TP / (TP + FN)
         </span>
       </p>
       <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
         <span style="font-size: 1.05rem; line-height: 2;">
           Precision = PPV = TP / (TP + FP)
         </span>
       </p>
     </section>
     <section style="margin-bottom: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Notes and Resources</h3>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li>Zhou et al. (2009) provide point estimates of the predictive values, as well as several approaches for computing their corresponding confidence intervals.</li>
         <li>The `BinomCI` function in the R package "DescTools" (Signorell et al., 2021) provides different methods (e.g., "wald", "agresti-coull", "wilson", "jeffreys", etc.) for calculating confidence intervals for a binomial proportion, assuming the dataset reflects the true disease prevalence in the general population. Refer to Brown et al. (2001) for a comparison of nine interval estimation methods for a binomial proportion.</li>
         <li>Note that PPV and NPV, as calculated using TP / (TP+FP) and TN/(TN+FN), respectively, are not intrinsic to the AI/ML system. For the same AI/ML system, using a test data set with a different disease prevalence will change the PPV and NPV. Zhou et al. (2009) and Mercaldo et al. (2007) provide methods for calculating point estimates and their corresponding confidence intervals for when the dataset does not reflect the true disease prevalence, but the true prevalence is known.</li>
         <li>Note that the interval estimation methods above assume all observations are independent (i.e., the occurrence of one event or observation does not affect the probability of occurrence of another). This assumption does not hold if, for example, the data includes multiple regions of interest from the same subject. For a discussion of confidence interval estimation for predictive values for clustered data, refer to Zhou et al. (2009).</li>
       </ul>
     </section>
     <section style="margin-bottom: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">References</h3>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li>Zhou, X. H., McClish, D. K., &amp; Obuchowski, N. A. (2009). <i>Statistical methods in Diagnostic Medicine</i> (Vol. 569). John Wiley &amp; Sons.</li>
         <li>Signorell, A. et al. (2021). DescTools: Tools for descriptive statistics. R package version 0.99.43.</li>
         <li>Brown, L. D., Cai, T. T., &amp; DasGupta, A. (2001). Interval estimation for a binomial proportion. <i>Statistical science, 16</i>(2), 101-133.</li>
         <li>Mercaldo, N. D., Lau, K. F., &amp; Zhou, X. H. (2007). Confidence intervals for predictive values with an emphasis to case-control studies. <i>Stat Med 26</i>(10): 2170-2183.</li>
       </ul>
     </section>
"""

_PPV_NPV = """
     <section style="margin-bottom: 1.5rem;">
       <h2 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 0.5rem; color: #1a202c;">Positive Predictive Value (PPV) and Negative Predictive Value (NPV)</h2>
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Definition</h3>
       <p style="color: #333; line-height: 1.6;"><b>Positive predictive value (PPV)</b> is the probability that an individual (or case, image, region of interest) is positive based on the reference standard when the AI/ML output is positive.</p>
       <p style="color: #333; line-height: 1.6;"><b>Negative predictive value (NPV)</b> is the probability that an individual (or case, image, region of interest) is negative based on the reference standard when the AI/ML output is negative.</p>
       <p style="color: #333; line-height: 1.6;">These are based on the following confusion matrix notations:</p>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li><b>TP</b> = true-positive decision</li>
         <li><b>FP</b> = false-positive decision</li>
         <li><b>TN</b> = true-negative decision</li>
         <li><b>FN</b> = false-negative decision</li>
       </ul>
     </section>
     <section style="margin-bottom: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Mathematical Formulation</h3>
       <p style="color: #333; line-height: 1.6;">PPV and NPV are mathematically defined as:</p>
       <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
         <span style="font-size: 1.05rem; line-height: 2;">
           PPV = TP / (TP + FP)
         </span>
       </p>
       <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
         <span style="font-size: 1.05rem; line-height: 2;">
           NPV = TN / (TN + FN)
         </span>
       </p>
     </section>
     <section style="margin-bottom: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Notes and Resources</h3>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li>Zhou et al. (2009) provide point estimates of the predictive values, as well as several approaches for computing their corresponding confidence intervals.</li>
         <li>The `BinomCI` function in the R package "DescTools" (Signorell et al., 2021) provides different methods (e.g., "wald", "agresti-coull", "wilson", "jeffreys", etc.) for calculating confidence intervals for a binomial proportion, assuming the dataset reflects the true disease prevalence in the general population. Refer to Brown et al. (2001) for a comparison of nine interval estimation methods for a binomial proportion.</li>
         <li>Note that PPV and NPV, as calculated using TP / (TP+FP) and TN/(TN+FN), respectively, are not intrinsic to the AI/ML system. For the same AI/ML system, using a test data set with a different disease prevalence will change the PPV and NPV. Zhou et al. (2009) and Mercaldo et al. (2007) provide methods for calculating point estimates and their corresponding confidence intervals for when the dataset does not reflect the true disease prevalence, but the true prevalence is known.</li>
         <li>Note that the interval estimation methods above assume all observations are independent (i.e., the occurrence of one event or observation does not affect the probability of occurrence of another). This assumption does not hold if, for example, the data includes multiple regions of interest from the same subject. For a discussion of confidence interval estimation for predictive values for clustered data, refer to Zhou et al. (2009).</li>
       </ul>
     </section>
     <section style="margin-bottom: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">References</h3>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li>Zhou, X. H., McClish, D. K., &amp; Obuchowski, N. A. (2009). <i>Statistical methods in Diagnostic Medicine</i> (Vol. 569). John Wiley &amp; Sons.</li>
         <li>Signorell, A. et al. (2021). DescTools: Tools for descriptive statistics. R package version 0.99.43.</li>
         <li>Brown, L. D., Cai, T. T., &amp; DasGupta, A. (2001). Interval estimation for a binomial proportion. <i>Statistical science, 16</i>(2), 101-133.</li>
         <li>Mercaldo, N. D., Lau, K. F., &amp; Zhou, X. H. (2007). Confidence intervals for predictive values with an emphasis to case-control studies. <i>Stat Med 26</i>(10): 2170-2183.</li>
       </ul>
     </section>
"""

_PLR_NLR = """
     <section style="margin-bottom: 1.5rem;">
       <h2 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 0.5rem; color: #1a202c;">Positive Likelihood Ratio (PLR) and Negative Likelihood Ratio (NLR)</h2>
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Definition</h3>
       <p style="color: #333; line-height: 1.6;"><b>Positive likelihood ratio (PLR)</b> is the ratio between the probability of correctly classifying an individual (or case, image, region of interest) that is positive based on the reference standard and the probability of incorrectly classifying an individual (or case, image, region of interest) that is negative based on the reference standard.</p>
       <p style="color: #333; line-height: 1.6;"><b>Negative likelihood ratio (NLR)</b> is the ratio between the probability of incorrectly classifying an individual (or case, image, region of interest) that is positive based on the reference standard and the probability of correctly classifying an individual (or case, image, region of interest) that is negative based on the reference standard.</p>
       <p style="color: #333; line-height: 1.6;">Unlike predictive values, PLR and NLR do <b>not</b> depend on the disease prevalence of positive (and negative) cases in the data set.</p>
       <p style="color: #333; line-height: 1.6;">These are based on the following confusion matrix notations:</p>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li><b>TP</b> = true-positive decision</li>
         <li><b>FP</b> = false-positive decision</li>
         <li><b>TN</b> = true-negative decision</li>
         <li><b>FN</b> = false-negative decision</li>
       </ul>
     </section>
     <section style="margin-bottom: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Mathematical Formulation</h3>
       <p style="color: #333; line-height: 1.6;">PLR and NLR are mathematically defined as:</p>
       <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
         <span style="font-size: 1.05rem; line-height: 2;">
           PLR = sensitivity / (1 &#8722; specificity)
         </span>
       </p>
       <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
         <span style="font-size: 1.05rem; line-height: 2;">
           NLR = (1 &#8722; sensitivity) / specificity
         </span>
       </p>
     </section>
     <section style="margin-bottom: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Notes and Resources</h3>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li>Zhou et al. (2009) provide point estimates of the positive and negative likelihood ratio, as well as several approaches for computing their corresponding confidence intervals.</li>
         <li>The `BinomRatioCI` function in the R package "DescTools" (Signorell et al., 2021) provides different methods for computing confidence intervals for the ratio of binomial proportions (including PLR and NLR).</li>
         <li>Note that the interval estimation methods above assume all observations are independent (i.e., the occurrence of one event or observation does not affect the probability of occurrence of another). This assumption does not hold if, for example, the data includes multiple regions of interest from the same subject.</li>
       </ul>
     </section>
     <section style="margin-bottom: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">References</h3>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li>Zhou, X. H., McClish, D. K., &amp; Obuchowski, N. A. (2009). <i>Statistical methods in Diagnostic Medicine</i> (Vol. 569). John Wiley &amp; Sons.</li>
         <li>Signorell, A. et al. (2021). DescTools: Tools for descriptive statistics. R package version 0.99.43.</li>
       </ul>
     </section>
"""

_MUTUAL_INFO = """
     <section style="margin-bottom: 1.5rem;">
       <h2 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 0.5rem; color: #1a202c;">Mutual Information</h2>
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Definition</h3>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li>In information theory, the <i>mutual information</i> of two random variables is a measure of the dependency between two variables, as originally defined by Shannon (1948) and Fano (Kreer, 1957).</li>
         <li>The concept of mutual information is closely related to that of <i>entropy</i> of a random variable, which is an information theory-based measure to quantify the amount of information in a random variable, and that of <i>joint entropy</i>, which measures the uncertainty associated with a set of variables.</li>
         <li>Given a discrete variable <i>x</i>, the <i>entropy</i> of <i>x</i> is defined as
           <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
             <span style="font-size: 1.05rem; line-height: 2;">
               <i>H</i>(<i>x</i>) = &#8722; <span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em; vertical-align: sub; margin-left: -0.3rem;"><i>x</i>&#8712;<i>X</i></sub> <i>p</i>(<i>x</i>) log <i>p</i>(<i>x</i>)
             </span>
           </p>
         </li>
         <li>Given two discrete variables <i>x</i> and <i>y</i>, the <i>joint entropy</i> between <i>x</i> and <i>y</i> is defined as
           <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
             <span style="font-size: 1.05rem; line-height: 2;">
               <i>H</i>(<i>x</i>,<i>y</i>) = &#8722; <span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em; vertical-align: sub; margin-left: -0.3rem;"><i>x</i>&#8712;<i>X</i></sub> <span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em; vertical-align: sub; margin-left: -0.3rem;"><i>y</i>&#8712;<i>Y</i></sub> <i>p</i>(<i>x</i>,<i>y</i>) log <i>p</i>(<i>x</i>,<i>y</i>)
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
         <li>In the defining formula above, if base-2 logarithm is applied, then the result is in <b>bits</b> (Metz et al., 1973). If the natural logarithm (i.e., base-e) is applied instead, the result will be in unit of <b>nats</b>.</li>
         <li>To apply <i>mutual information</i> to a classification problem, we interpret <i>x</i> as the <i>true</i> class label and x&#x0302; as the predicted class label:
           <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
             <span style="font-size: 1.05rem; line-height: 2;">
               <i>I</i>(<i>x</i>, x&#x0302;) = <i>H</i>(<i>x</i>) &#8722; <i>H</i>(<i>x</i>&#124;x&#x0302;)
             </span>
           </p>
         </li>
         <li>Mutual information for a diagnostic test is the amount of information expected to be gained by a diagnostic test, i.e., the difference between pre-test uncertainty and post-test uncertainty (Metz et al., 1973).</li>
         <li>In the context of an AI/ML model, mutual information can be interpreted as the amount of information expected to be gained by the information provided by the model, i.e., the difference between the uncertainty before observing the AI/ML output and the uncertainty after observing the AI/ML output.</li>
       </ul>
     </section>
     <section style="margin-bottom: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Mutual information for a binary classification task</h3>
       <p style="color: #333; line-height: 1.6;">For a binary classification task, it is convenient to express the 2x2 confusion matrix as shown in the Overview section above.</p>
       <p style="color: #666; font-style: italic; line-height: 1.6; margin-top: 0.5rem;">Note: In the confusion table, the reference standard is represented in columns and AI/ML predictions in rows. If your table uses a reversed convention (rows for reference standard, columns for predictions), the <i>n</i><sub style="font-size: 0.75em;">ij</sub> expressions for TP, TN, FP, and FN should be adjusted accordingly.</p>
       <p style="color: #333; line-height: 1.6; margin-top: 1rem;">where:</p>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li><i>n</i><sub style="font-size: 0.75em;">11</sub> = TP = true-positive decision</li>
         <li><i>n</i><sub style="font-size: 0.75em;">12</sub> = FP = false-positive decision</li>
         <li><i>n</i><sub style="font-size: 0.75em;">21</sub> = FN = false-negative decision</li>
         <li><i>n</i><sub style="font-size: 0.75em;">22</sub> = TN = true-negative decision</li>
       </ul>
       <p style="color: #333; line-height: 1.6; margin-top: 1rem;">The entropies of <i>x</i> and the predicted label and their joint entropy can then be expressed as below:</p>
       <p style="color: #333; line-height: 1.6; margin-top: 0.5rem;"><b>The entropy of the ground truth distribution:</b></p>
       <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
         <span style="font-size: 1.05rem; line-height: 2;">
           <i>H</i>(<i>x</i>) = &#8722;[<i>P</i>(<i>x</i>=1) log <i>P</i>(<i>x</i>=1) + <i>P</i>(<i>x</i>=0) log <i>P</i>(<i>x</i>=0)]<br>
           = &#8722;[((TP + FN)/<i>N</i>) &#183; log((TP + FN)/<i>N</i>) + ((FP + TN)/<i>N</i>) &#183; log((FP + TN)/<i>N</i>)]
         </span>
       </p>
       <p style="color: #333; line-height: 1.6; margin-top: 0.5rem;"><b>The entropy of the classifier's predictions:</b></p>
       <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
         <span style="font-size: 1.05rem; line-height: 2;">
           <i>H</i>(x&#x0302;) = &#8722;[<i>P</i>(x&#x0302;=1) log <i>P</i>(x&#x0302;=1) + <i>P</i>(x&#x0302;=0) log <i>P</i>(x&#x0302;=0)]<br>
           = &#8722;[((TP + FP)/<i>N</i>) &#183; log((TP + FP)/<i>N</i>) + ((FN + TN)/<i>N</i>) &#183; log((FN + TN)/<i>N</i>)]
         </span>
       </p>
       <p style="color: #333; line-height: 1.6; margin-top: 0.5rem;"><b>Joint entropy:</b></p>
       <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
         <span style="font-size: 1.05rem; line-height: 2;">
           <i>H</i>(<i>x</i>,x&#x0302;) = &#8722; <span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em; vertical-align: sub; margin-left: -0.3rem;"><i>x</i>&#8712;{0,1}</sub> <span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em; vertical-align: sub; margin-left: -0.3rem;">x&#x0302;&#8712;{0,1}</sub> <i>P</i>(<i>x</i>,x&#x0302;) log&#8322; <i>P</i>(<i>x</i>,x&#x0302;)<br>
           = &#8722;[(TP/<i>N</i>) &#183; log(TP/<i>N</i>) + (FN/<i>N</i>) &#183; log(FN/<i>N</i>) + (FP/<i>N</i>) &#183; log(FP/<i>N</i>) + (TN/<i>N</i>) &#183; log(TN/<i>N</i>)]
         </span>
       </p>
       <p style="color: #333; line-height: 1.6; margin-top: 1rem;">The mutual information is expressed as below:</p>
       <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
         <span style="font-size: 1.05rem; line-height: 2;">
           <i>I</i>(<i>x</i>, x&#x0302;) = <i>H</i>(<i>x</i>) + <i>H</i>(x&#x0302;) &#8722; <i>H</i>(<i>x</i>,x&#x0302;)
         </span>
       </p>
       <p style="color: #333; line-height: 1.6; margin-top: 1rem;">An equivalent expression for mutual information, used by Hughes et al. (2020) is:</p>
       <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
         <span style="font-size: 1.05rem; line-height: 2;">
           <i>I</i>(<i>x</i>, x&#x0302;) = <span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em; vertical-align: sub; margin-left: -0.3rem;"><i>i</i>=1</sub><sup style="font-size: 0.65em; vertical-align: super; margin-left: -0.5rem;">2</sup> <span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em; vertical-align: sub; margin-left: -0.3rem;"><i>j</i>=1</sub><sup style="font-size: 0.65em; vertical-align: super; margin-left: -0.5rem;">2</sup> <i>p</i>(<i>x</i><sub style="font-size: 0.7em;">i</sub>, x&#x0302;<sub style="font-size: 0.7em;">j</sub>) log[<i>p</i>(<i>x</i><sub style="font-size: 0.7em;">i</sub>, x&#x0302;<sub style="font-size: 0.7em;">j</sub>) / (<i>p</i>(<i>x</i><sub style="font-size: 0.7em;">i</sub>) <i>p</i>(x&#x0302;<sub style="font-size: 0.7em;">j</sub>))]
         </span>
       </p>
       <p style="color: #333; line-height: 1.6;">This form can be expressed in terms of sensitivity, specificity, and prevalence. Refer to the resources by Hughes et al. (2020) or Metz et al. (1973) for the full expressions.</p>
       <p style="color: #333; line-height: 1.6; margin-top: 1rem;">Some efforts have been made to describe Bayesian estimators for mutual information (Archer et al., 2013).</p>
       <p style="color: #333; line-height: 1.6;">The R package 'entropy' (<a href="https://cran.r-project.org/web/packages/entropy/entropy.pdf" target="_blank" style="color: #2b6cb0; text-decoration: underline;">https://cran.r-project.org/web/packages/entropy/entropy.pdf</a>) can be used to compute the estimate of entropy and mutual information.</p>
     </section>
     <section style="margin-bottom: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Normalized mutual information for a binary classification task</h3>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li>Note that <i>I</i>(<i>x</i>, x&#x0302;) varies between 0 and <i>H</i>(<i>x</i>). If the predicted labels do not provide any information about the true labels, then <i>H</i>(<i>x</i>&#124;x&#x0302;) = <i>H</i>(<i>x</i>) (the amount of information needed to describe <i>x</i> after observing predicted label is still <i>H</i>(<i>x</i>)), and thus <i>I</i>(<i>x</i>,x&#x0302;) = 0. If the predicted labels provide perfect information about the true labels, then <i>H</i>(<i>x</i>&#124;x&#x0302;) = 0 (the amount of information needed to describe <i>x</i> after observing predicted label is 0), and thus <i>I</i>(<i>x</i>, x&#x0302;) = <i>H</i>(<i>x</i>).</li>
         <li>To provide a metric that is independent of the entropy of the true labels, mutual information can therefore be normalized with <i>H</i>(<i>x</i>), yielding a metric value between 0 and 1. This metric is named normalized mutual information (Baldi et al., 2000), and defined as follows:
           <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
             <span style="font-size: 1.05rem; line-height: 2;">
               NMI = <i>I</i>(<i>x</i>, x&#x0302;) / <i>H</i>(<i>x</i>)
             </span>
           </p>
         </li>
       </ul>
     </section>
     <section style="margin-bottom: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">References</h3>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li>Shannon, C. E. (1948). A mathematical theory of communication. The Bell system technical journal, 27(3), 379-423.</li>
         <li>Kreer, J. (1957). A question of terminology. IRE Transactions on Information Theory, 3(3), 208-208.</li>
         <li>Metz, C. E., Goodenough, D. J., &amp; Rossmann, K. (1973). Evaluation of receiver operating characteristic curve data in terms of information theory, with applications in radiography. Radiology, 109(2), 297-303.</li>
         <li>Baldi, P., Brunak, S., Chauvin, Y., Andersen, C. A., &amp; Nielsen, H. (2000). Assessing the accuracy of prediction algorithms for classification: an overview. Bioinformatics, 16(5), 412-424.</li>
         <li>Hughes, G, Kopetzky J, &amp; McRoberts N. (2020). Mutual Information as a Performance Measure for Binary Predictors Characterized by Both ROC Curve and PROC Curve Analysis. <i>Entropy 22</i>, no. 9: 938.</li>
         <li>Archer, E., Park, I. M., &amp; Pillow, J. W. (2013) Bayesian and quasi-Bayesian estimators for mutual information from discrete data. <i>Entropy, vol. 15</i>, no. 5, pp. 1738-1755.</li>
       </ul>
     </section>
"""

_YOUDEN = """
     <section style="margin-bottom: 1.5rem;">
       <h2 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 0.5rem; color: #1a202c;">Youden Index</h2>
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Definition</h3>
       <p style="color: #333; line-height: 1.6;">The <b>Youden index</b> (Youden, 1950) (<i>J</i>) is a measure based on sensitivity and specificity. Mathematically:</p>
       <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
         <span style="font-size: 1.05rem; line-height: 2;">
           <i>J</i> = sensitivity + specificity &#8722; 1
         </span>
       </p>
     </section>
     <section style="margin-bottom: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Notes and Resources</h3>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li>Shan (2015) proposed two approaches to construct confidence intervals using the square-and-add limits based on the Wilson score method, and compared them to bootstrapping methods. The code for this article can be found at gshan.faculty.unlv.edu/Rcode/CI_YoudenIndex.r. Please note that the referred library 'parallel' in the code has been enhanced to 'parallelly'.</li>
       </ul>
     </section>
     <section style="margin-bottom: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">References</h3>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li>Youden, W. J. (1950). Index for rating diagnostic tests. <i>Cancer, 3</i>(1), 32&#8211;35.</li>
         <li>Shan, G. (2015). Improved confidence intervals for the Youden index. <i>PloS one, 10</i>(7), e0127272.</li>
       </ul>
     </section>
"""

_F1 = """
     <section style="margin-bottom: 1.5rem;">
       <h2 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 0.5rem; color: #1a202c;">F1 Score</h2>
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Definition</h3>
       <p style="color: #333; line-height: 1.6;">The <b>F1 score</b> is the harmonic mean of the precision (sensitivity) and recall (positive predictive value).</p>
       <p style="color: #333; line-height: 1.6;">The F1 score represents a balancing act between precision and recall on the positive class. This is particularly important for imbalanced problems (e.g., problems with large numbers of true negatives, where accuracy is always very high). The F1 score combines precision and recall into one metric by calculating their harmonic mean.</p>
       <p style="color: #333; line-height: 1.6;">The F1 score is a special case of a more general function <i>F</i><sub style="font-size: 0.75em;">&#946;</sub>:</p>
       <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
         <span style="font-size: 1.05rem; line-height: 2;">
           <i>F</i><sub style="font-size: 0.7em;">&#946;</sub> = (1 + &#946;&#178;) &#183; [precision &#183; recall] / [(&#946;&#178; &#183; precision) + recall]
         </span>
       </p>
       <p style="color: #333; line-height: 1.6;">For example, the F2 score weights recall twice as important as precision:</p>
       <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
         <span style="font-size: 1.05rem; line-height: 2;">
           F2 = 5 &#183; [precision &#183; recall] / [(4 &#183; precision) + recall]
         </span>
       </p>
       <p style="color: #333; line-height: 1.6;">Similarly, the beta value can be set to a value between 0 and 1 when precision, rather than recall, is more important.</p>
     </section>
     <section style="margin-bottom: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Notes and Resources</h3>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li>Wang et al. (2014) proposed a method to compute the confidence interval for the F1 score, based on the original work of Goutte and Gaussier (2005).</li>
         <li>The R package 'MLmetrics' also includes a function to compute the F1 score (`F1_Score`).</li>
       </ul>
     </section>
     <section style="margin-bottom: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">References</h3>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li>Wang, Y., Li, J., Li, Y., Wang, R., &amp; Yang, X. (2014). Confidence Interval for F1 Measure of Algorithm Performance Based on Blocked 3*2 Cross-Validation. <i>IEEE Transactions on Knowledge and Data Engineering, 27</i>(3), 651-659.</li>
         <li>Goutte, C., &amp; Gaussier, E. (2005). A probabilistic interpretation of precision, recall F score, with implication for evaluation. In <i>Proc. Eur. Colloq. IR Res.</i>, pp. 345-359.</li>
       </ul>
     </section>
"""


_MCC = """
     <section style="margin-bottom: 1.5rem;">
       <h2 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 0.5rem; color: #1a202c;">Matthews Correlation Coefficient (MCC)</h2>
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Definition</h3>
       <p style="color: #333; line-height: 1.6;">Matthews Correlation Coefficient (MCC) was originally introduced by Brian W. Matthews in 1975 (Matthews, 1975) as a metric for binary classification problems. For a binary classification problem, it is equivalent to the sample Pearson's correlation coefficient. The mathematical formula (Elloumi et al., 2008) is as follows:</p>
       <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
         <span style="font-size: 1.05rem; line-height: 2;">
           MCC = [(TP &#183; TN) &#8722; (FP &#183; FN)] / &#8730;[(TP+FP)(TP+FN)(TN+FP)(TN+FN)]
         </span>
       </p>
       <p style="color: #333; line-height: 1.6;">This is based on the following confusion matrix notations:</p>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li><b>TP</b> = true-positive decision</li>
         <li><b>FP</b> = false-positive decision</li>
         <li><b>TN</b> = true-negative decision</li>
         <li><b>FN</b> = false-negative decision</li>
       </ul>
     </section>
     <section style="margin-bottom: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Notes and Resources</h3>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li>The range of MCC is [&#8722;1, 1].</li>
         <li>MCC is generally regarded as a balanced measure that can be used in <b>binary</b> classification even when the sizes of classes are very different (Chicco &amp; Jurman, 2020).</li>
         <li>The R function `mcc` in the 'mltools' package and the Python function "sklearn.metrics.matthews_corrcoef" can be used to compute the estimate of MCC.</li>
       </ul>
     </section>
     <section style="margin-bottom: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">References</h3>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li>Matthews, B. W. (1975). Comparison of the predicted and observed secondary structure of T4 phage lysozyme. <i>Biochimica et Biophysica Acta (BBA)-Protein Structure, 405</i>(2), 442-451.</li>
         <li>Elloumi, M., K&#252;ng, J., Linial, M., Murphy, R., Schneider, K., &amp; Toma, C. (Eds.). (2008). <i>Bioinformatics Research and Development: Second International Conference, BIRD 2008, Vienna, Austria, July 7-9, 2008 Proceedings</i> (Vol. 13). (Page 150). Springer Science &amp; Business Media.</li>
         <li>Chicco, D., &amp; Jurman, G. (2020). The advantages of the Matthews correlation coefficient (MCC) over F1 score and accuracy in binary classification evaluation. <i>BMC genomics, 21</i>(1), 1-13.</li>
       </ul>
     </section>
"""

_KAPPA = """
     <section style="margin-bottom: 1.5rem;">
       <h2 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 0.5rem; color: #1a202c;">Cohen's Kappa</h2>
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Definition</h3>
       <p style="color: #333; line-height: 1.6;">Cohen's Kappa was originally proposed by Cohen in 1960 (1) in order to measure the agreement between two raters for categorical items, by taking into account the possibility of the agreement occurring by chance.</p>
       <p style="color: #333; line-height: 1.6;">The original definition for Cohen's Kappa is</p>
       <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
         <span style="font-size: 1.05rem; line-height: 2;">
           &#954; = (p<sub style="font-size: 0.7em;">o</sub> &#8722; p<sub style="font-size: 0.7em;">e</sub>) / (1 &#8722; p<sub style="font-size: 0.7em;">e</sub>)
         </span>
       </p>
       <p style="color: #333; line-height: 1.6;">where p<sub style="font-size: 0.75em;">o</sub> is the relative <b>observed</b> agreement among raters, p<sub style="font-size: 0.75em;">e</sub> is the hypothetical probability of chance agreement.</p>
       <p style="color: #333; line-height: 1.6;">Later, Cohen's Kappa was also used as a performance metric for binary classification problems. The defining formula is given as following (2)</p>
       <p style="text-align: center; margin: 1rem 0; padding: 1rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
         <span style="font-size: 1.05rem; line-height: 2;">
           &#954; = [2(TP &#183; TN &#8722; FN &#183; FP)] / [(TP + FP)(FP + TN) + (TP + FN)(FN + TN)]
         </span>
       </p>
       <p style="color: #333; line-height: 1.6;">based on the following confusion matrix notations:</p>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li><b>TP</b> = true-positive decision</li>
         <li><b>FP</b> = false-positive decision</li>
         <li><b>TN</b> = true-negative decision</li>
         <li><b>FN</b> = false-negative decision</li>
       </ul>
     </section>
     <section style="margin-bottom: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Notes and Resources</h3>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li>Cohen's Kappa is generally thought to be a more robust measure than simple percent agreement calculation, as Kappa takes into account the possibility of the agreement occurring by chance. On the other side, there is also controversy (3) about Cohen's kappa due to the difficulty in interpreting indices of agreement, and because of the difficulty of summarizing a contingency table using a single number, a difficulty shared by other single-number metrics for classification.</li>
         <li>The range of Cohen's Kappa is [&#8722;1, 1].</li>
         <li>Note that there are different versions of interpretation for the degree of agreement based on Kappa value, for example, (1) and (4).</li>
         <li>Cohen (1) gave an expression for standard deviation for Cohen's Kappa, based on which and normality distributional assumption, one can estimate confidence interval for Cohen's Kappa. Though this expression was considered by Fleiss, Cohen, and Everitt (5) to be an approximation based on faulty assumptions, it is still often used for planning purposes. PASS Sample Size Software provided by NCSS.com includes a Kappa calculation tool that allows computation of both versions of standard deviation for Cohen's Kappa (i.e., Cohen's version versus Fleiss' more accurate version), and they have found that the two version are often close. Interested readers are referred to (6) for more details.</li>
         <li>R package "psych" (<a href="https://www.rdocumentation.org/packages/psych/versions/2.1.9/topics/cohen.kappa" target="_blank" style="color: #2b6cb0; text-decoration: underline;">https://www.rdocumentation.org/packages/psych/versions/2.1.9/topics/cohen.kappa</a>) provides functions to compute point estimate and confidence interval for Cohen's Kappa.</li>
         <li>R package 'irr' (<a href="https://cran.r-project.org/web/packages/irr/irr.pdf" target="_blank" style="color: #2b6cb0; text-decoration: underline;">https://cran.r-project.org/web/packages/irr/irr.pdf</a>) also provides functions to compute estimate for Cohen's Kappa.</li>
       </ul>
     </section>
     <section style="margin-bottom: 1.5rem;">
       <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">References</h3>
       <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
         <li>1. Cohen, Jacob (1960). "A coefficient of agreement for nominal scales". <i>Educational and Psychological Measurement. 20</i>(1): 37&#8211;46.</li>
         <li>2. Bielza, C., &amp; Larra&#241;aga, P. (2020). <i>Data-driven computational neuroscience: machine learning and statistical models</i>. (Page 205). Cambridge University Press.</li>
         <li>3. Guggenmoos-Holzmann, I. (1996). The meaning of kappa: probabilistic concepts of reliability and validity revisited. <i>Journal of clinical epidemiology, 49</i>(7), 775-782.</li>
         <li>4. McHugh, M. L. (2012). Interrater reliability: the kappa statistic. <i>Biochemia medica, 22</i>(3), 276-282.</li>
         <li>5. Fleiss, J. L., Cohen, J., &amp; Everitt, B. S. (1969). Large sample standard errors of kappa and weighted kappa. <i>Psychological bulletin, 72</i>(5), 323.</li>
         <li>6. NCSS.com (assessed 2022, Feb 16). PASS Sample Size Software.</li>
         <li>7. Cohen, J. (1968). Weighted kappa: nominal scale agreement provision for scaled disagreement or partial credit. <i>Psychological bulletin, 70</i>(4), 213.</li>
       </ul>
     </section>
"""

NODE = {
    "id": "N0_2",
    "title": "Binary classification \u2013 metrics based on 2x2 matrix",
    "type": "metric_selector",
    "overview_html": _OVERVIEW,
    "metrics": {
        "Se, Sp (Sensitivity, Specificity)": {
            "html": _SE_SP, "latex": []},
        "Precision, recall": {
            "html": _PRECISION_RECALL, "latex": []},
        "PPV, NPV (Positive Predictive Value, Negative Predictive Value)": {
            "html": _PPV_NPV, "latex": []},
        "PLR, NLR (Positive Likelihood Ratio, Negative Likelihood Ratio)": {
            "html": _PLR_NLR, "latex": []},
        "Mutual info (Mutual Information)": {
            "html": _MUTUAL_INFO, "latex": []},
        "Youden index": {
            "html": _YOUDEN, "latex": []},
        "F1 score": {
            "html": _F1, "latex": []},
        "Matthews corr coeff (Matthews Correlation Coefficient)": {
            "html": _MCC, "latex": []},
        "Cohen's kappa": {
            "html": _KAPPA, "latex": []},
    },
}
