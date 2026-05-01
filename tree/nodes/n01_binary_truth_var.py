# tree/nodes/n01_binary_truth_var.py

NODE = {
    "id": "N0_1",
    "title": "Binary classification \u2013 metrics based on percent agreement and interchangeability",
    "type": "content",
    "content_html": """
  <section style="margin-bottom: 1.5rem;">
   <h2 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 0.5rem; color: #1a202c;">Overview</h2>
   <p style="color: #333; line-height: 1.6;">You have identified your task as a <i>binary</i> classification task based on a <i>reference standard with non-negligible unreliability and variability</i>. Currently, there is a lack of widely acknowledged performance evaluation metric used for this context. Please read the following for a summary of evaluation metrics/methods applicable to this scenario.</p>
  </section>
  <section style="margin-bottom: 1.5rem;">
   <h2 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 0.5rem; color: #1a202c;">Evaluation metrics/approaches for binary classification with truth variability</h2>
   <p style="color: #dc2626; font-weight: bold; line-height: 1.6;">Highlight message</p>
   <p style="color: #333; line-height: 1.6;">Evaluation of classification models often relies on a perfect ground truth, which may not be available in many real-world scenarios. This leads to truth variability which poses a challenge for evaluating classification tasks. In this discussion, we present three (but not all) approaches&#8212;percent agreement metrics, interchangeability metric, and latent class analysis&#8212;to address this issue. It is important to note that no universally accepted evaluation metric exists for classification tasks with truth variability, and the presented approaches are intended as starting points to explore this area. <strong>However, it is essential to remember that these methods should not replace the gold standard test, which remains the ideal reference standard for evaluation.</strong></p>
  </section>
  <section style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Background</h3>
   <p style="color: #333; line-height: 1.6;">When evaluating the performance of a classification model, it is common practice to compare the predicted labels of the model with the ground truth labels. Ideally, the ground truth should be established using a gold standard, which is an error-free reference standard (STARD, Cohen et al., 2016). However, in many classification tasks, such as medical imaging, the ground truth is often determined by human experts, leading to variability in the established truth.</p>
   <p style="color: #333; line-height: 1.6;">Existing studies on binary classification evaluation metrics mostly assume a perfect ground truth, with very few studies accounting for truth variability. As a result, there is no consensus approach to evaluation metrics for classification tasks with truth variability. In this summary, we provide an overview of some existing solutions in different categories, with the hope that readers can use this as a starting point to find the most suitable evaluation metric/method for their specific task. <strong>It is important to note that these methods should never be seen as substitutes for a gold standard test, as the gold standard is always the ideal choice (Albert and Dodd, 2004).</strong></p>
  </section>
  <section style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Percent agreement metrics</h3>
   <p style="color: #333; line-height: 1.6;">One approach is to extend the traditional (sensitivity, specificity) pair to evaluate the classifier in comparison to a non-reference standard (FDA CDRH, 2007). The generalized metrics are known as Positive Percent Agreement (PPA) and Negative Percent Agreement (NPA). PPA represents the proportion of non-reference standard positive subjects in whom the new test is positive, and NPA represents the proportion of non-reference standard negative subjects in whom the new test is negative. These metrics provide numerical calculations similar to sensitivity and specificity and can be considered counterparts of (Se, Sp) in the absence of a reference standard. However, the terms sensitivity and specificity are not appropriate to describe the comparative results here, because one cannot directly calculate unbiased estimates of sensitivity and specificity when the new test is evaluated by comparison to a non-reference standard test. Instead, the estimates are named as PPA and NPA.</p>
  </section>
  <section style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Interchangeability metric</h3>
   <p style="color: #333; line-height: 1.6;">Another approach is to quantify the degree of agreement/interchangeability between the classifier being evaluated and a comparator classifier. An example of this type is a metric proposed by Obuchowski et al. (2014), called <i>individual equivalence index</i>, which can be considered as an extension of <i>individual bioequivalence</i> (i.e., a measure of bioequivalence between drug products) (FDA CDER, 2001), to the setting of diagnostic imaging testing comparison. This index measures how closely the agreement between a new classifier <i>T</i> and a comparator test <i>R</i> aligns with the agreement among replicate outcomes based on the comparator test <i>R</i> itself. It requires obtaining replicate measurements from the comparator test. To determine whether the two classifiers <i>T</i> and <i>R</i> are interchangeable, hypothesis testing can be performed to compare the index estimate with a pre-specified threshold. Mathematically, the <b>individual equivalence index</b> is defined as below.</p>
   <p style="text-align: center; margin: 1.5rem 0; padding: 1.5rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
    <span style="font-size: 1.05rem; line-height: 2.2;">
     &#947;<sub style="font-size: 0.7em;">(p)</sub> = Prob(<i>Y</i><sub style="font-size: 0.7em;">iRjk</sub> = <i>Y</i><sub style="font-size: 0.7em;">iRjk'</sub>) &#8722; Prob(<i>Y</i><sub style="font-size: 0.7em;">iTjk</sub> = <i>Y</i><sub style="font-size: 0.7em;">iRjk</sub>)
    </span>
   </p>
   <p style="color: #333; line-height: 1.6;">where Prob(<i>Y</i><sub style="font-size: 0.75em;">iRjk</sub> = <i>Y</i><sub style="font-size: 0.75em;">iRjk'</sub>) is the probability how replicate outcomes based on the comparator test <i>R</i> itself at two occasions (<i>jk</i> vs. <i>jk'</i>) agree with each other, and Prob(<i>Y</i><sub style="font-size: 0.75em;">iTjk</sub> = <i>Y</i><sub style="font-size: 0.75em;">iRjk</sub>) is the probability how the results of the classifier to be evaluated <i>T</i> for subject <i>i</i> agree with those from the comparator classifier <i>R</i>.</p>
   <p style="color: #333; line-height: 1.6; font-weight: bold;">Remark:</p>
   <p style="color: #333; line-height: 1.6;">Example of application: Now consider an example where we investigate if an AI classifier <i>T</i> is interchangeable with a set of <i>J</i> truthers/radiologists <i>R</i><sub style="font-size: 0.75em;">1</sub>,...,<i>R</i><sub style="font-size: 0.75em;">j</sub>. Denote the measurement for subject <i>i</i> based on AI classifier <i>T</i> and truther <i>R</i><sub style="font-size: 0.75em;">j</sub> as <i>Y</i><sub style="font-size: 0.75em;">iT</sub> and <i>Y</i><sub style="font-size: 0.75em;">iRj</sub> respectively. For practical reasons, we regard the measurements from <i>J</i> truthers for the same subject as replicate measurements based on the same comparator method (i.e., human experts), even though they are from different truthers and it is difficult to have repeated measurements for the same subject from each of all truthers. Under this assumption, we could apply approach in Obuchowski et al. (2014) to estimate the <i>probabilistic individual equivalence index</i>. The estimated index is shown below.</p>
   <p style="text-align: center; margin: 1.5rem 0; padding: 1.5rem; background-color: #f5f5f5; border-left: 4px solid #2b6cb0; font-family: 'Times New Roman', serif;">
    <span style="font-size: 1.0rem; line-height: 1.8;">
     &#947;&#770;<sub style="font-size: 0.7em;">(p)</sub> =
     (1/<i>NJ</i>) <span style="font-size: 1.3rem; vertical-align: middle;">&#8721;</span><sub style="font-size: 0.65em; vertical-align: sub; margin-left: -0.3rem;"><i>i</i>=1</sub><sup style="font-size: 0.65em; vertical-align: super; margin-left: -0.5rem;"><i>N</i></sup>
     <span style="font-size: 1.3rem; vertical-align: middle; margin-left: 0.2rem;">&#8721;</span><sub style="font-size: 0.65em; vertical-align: sub; margin-left: -0.3rem;"><i>j</i>=1</sub><sup style="font-size: 0.65em; vertical-align: super; margin-left: -0.5rem;"><i>J</i></sup>
     <i>I</i>{<i>Y</i><sub style="font-size: 0.7em;">iT</sub> = <i>Y</i><sub style="font-size: 0.7em;">iRj</sub>}
     &#8722; (1/[<i>NJ</i>(<i>J</i>&#8722;1)])
     <span style="font-size: 1.3rem; vertical-align: middle; margin-left: 0.2rem;">&#8721;</span><sub style="font-size: 0.65em; vertical-align: sub; margin-left: -0.3rem;"><i>i</i>=1</sub><sup style="font-size: 0.65em; vertical-align: super; margin-left: -0.5rem;"><i>N</i></sup>
     <span style="font-size: 1.3rem; vertical-align: middle; margin-left: 0.2rem;">&#8721;</span><sub style="font-size: 0.65em; vertical-align: sub; margin-left: -0.3rem;"><i>j</i>=1</sub><sup style="font-size: 0.65em; vertical-align: super; margin-left: -0.5rem;"><i>J</i></sup>
     <span style="font-size: 1.3rem; vertical-align: middle; margin-left: 0.2rem;">&#8721;</span><sub style="font-size: 0.55em; vertical-align: sub; margin-left: -0.3rem;"><i>j</i>'=1, <i>j</i>'&#8800;<i>j</i></sub><sup style="font-size: 0.65em; vertical-align: super; margin-left: -0.5rem;"><i>J</i></sup>
     <i>I</i>{<i>Y</i><sub style="font-size: 0.7em;">iRj</sub> = <i>Y</i><sub style="font-size: 0.7em;">iRj'</sub>}
    </span>
   </p>
   <p style="color: #333; line-height: 1.6;">where <i>I</i>{.} is an indicator function which takes value of 1 if true and 0 otherwise.</p>
   <p style="color: #333; line-height: 1.6; font-weight: bold;">Remark:</p>
   <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
    <li>The example above serves only for illustrative purposes, and the estimation formula provided may differ from the one in Obuchowski et al. (2014) due to variations in the problem setting and study design. For different problem settings, the estimation formula needs to be adapted accordingly.</li>
    <li>The appendix of Obuchowski et al. (2014) describes a procedure for constructing a 95% confidence interval for the estimate.</li>
   </ul>
  </section>
  <section style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Latent class analysis</h3>
   <p style="color: #333; line-height: 1.6;">A third approach is based on latent class analysis, a statistical method for identifying latent ("hidden", opposed to observed variables) class membership among subjects using observed variables (Nylund, 2021). This approach has been employed in evaluating diagnostic tests when a gold standard diagnosis is unavailable, by treating the true diagnosis result as a latent variable. Some latent class models (e.g., Hui and Walter, 1980) assume conditional independence, meaning the test results are independent given the true status (Albert and Dodd, 2004). However, this assumption may not hold in many applications, and when violated, the inferences for diagnostic accuracy can be biased (Torrance-Rynard and Walter, 1997). Hadgu and Qu (1998) described an approach that extends traditional latent class models to account for random effects and covariates, relaxing the conditional independence assumption. A note from Albert and Dodd (2004) examined the robustness of inferences about diagnostic accuracy to assumptions on the dependence structure between tests, and showed that the inferences are biased when the dependence structure is mis-specified.</p>
   <p style="color: #333; line-height: 1.6;">Latent class analysis has also been applied in the context of crowdsourcing to infer the true label and predict the capability of crowdsourcing workers in classification tasks when the true label is unavailable. This problem is similar to the one discussed here, where the workers in crowdsourcing setting can be viewed as readers/radiologists in a diagnostic study. References in this application area include Raykar et al. (2010), Gao and Zhou (2013), and Zhang et al. (2016). However, many studies in the area of crowdsourcing assume conditional independence, which is a limitation.</p>
  </section>
  <section style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">Discussion</h3>
   <p style="color: #333; line-height: 1.6;">In addition to the three approaches above, there may be other types of evaluation methods for classification tasks accounting for truth variabilities, considered that this area is evolving dynamically. However, it is important to note that currently there is no single universally accepted evaluation metric for classification task with truth variability, given the scarce of literature in this area. By providing information about these options, our aim is to offer a starting point for users to investigate the best option for their specific needs, rather than making a specific recommendation.</p>
  </section>
  <section style="margin-bottom: 1.5rem;">
   <h3 style="font-size: 1.25rem; font-weight: 600; margin-bottom: 0.5rem; color: #1a202c;">References</h3>
   <ul style="list-style-type: disc; margin-left: 1.5rem; color: #333;">
    <li>Albert, P. S., &amp; Dodd, L. E. (2004). A cautionary note on the robustness of latent class models for estimating diagnostic error without a gold standard. Biometrics, 60(2), 427-435.</li>
    <li>Cohen, J. F., Korevaar, D. A., Altman, D. G., Bruns, D. E., Gatsonis, C. A., Hooft, L., ... &amp; Bossuyt, P. M. (2016). STARD 2015 guidelines for reporting diagnostic accuracy studies: explanation and elaboration. BMJ open, 6(11), e012799.</li>
    <li>FDA CDRH. (2007). Guidance for Industry and FDA Staff Statistical Guidance on Reporting Results from Studies Evaluating Diagnostic Tests. FDA. Retrieved from <a href="https://www.fda.gov/media/71147/download" target="_blank" style="color: #2b6cb0; text-decoration: underline;">https://www.fda.gov/media/71147/download</a> (accessed on May 25, 2022).</li>
    <li>FDA CDER. (2001, Jan). Guidance for Industry - Statistical Approaches to Establishing Bioequivalence. FDA. Retrieved from <a href="https://www.fda.gov/media/70958/download" target="_blank" style="color: #2b6cb0; text-decoration: underline;">https://www.fda.gov/media/70958/download</a> (assessed on April 5, 2022).</li>
    <li>Gao, C., &amp; Zhou, D. (2013). Minimax optimal convergence rates for estimating ground truth from crowdsourced labels. arXiv preprint arXiv:1310.5764.</li>
    <li>Hadgu, A., &amp; Qu (1998). A biomedical application of latent class models with random effects. Journal of the Royal Statistical Society: Series C (Applied Statistics), 47(4), 603-616.</li>
    <li>Hui, S. L., &amp; Walter, S. D. (1980). Estimating the error rates of diagnostic tests. Biometrics, 167-171.</li>
    <li>Nylund, K. (2021). Latent Class Analysis in Mplus Version 3 [Powerpoint file archived]. Retrieved from <a href="https://stats.oarc.ucla.edu/mplus/seminars/lca/" target="_blank" style="color: #2b6cb0; text-decoration: underline;">https://stats.oarc.ucla.edu/mplus/seminars/lca/</a> on June 8, 2022.</li>
    <li>Obuchowski, N. A., Subhas, N., &amp; Schoenhagen, P. (2014). Testing for interchangeability of imaging tests. Academic Radiology, 21(11), 1483-1489.</li>
    <li>Raykar, V. C., Yu, S., Zhao, L. H., Valadez, G. H., Florin, C., Bogoni, L., &amp; Moy, L. (2010). Learning from crowds. Journal of machine learning research, 11(4).</li>
    <li>Torrance&#8208;Rynard, V. L., &amp; Walter, S. D. (1997). Effects of dependent errors in the assessment of diagnostic test performance. Statistics in medicine, 16(19), 2157-2175.</li>
    <li>Zhang, Y., Chen, X., Zhou, D., &amp; Jordan, M. I. (2016). Spectral methods meet EM: A provably optimal algorithm for crowdsourcing. The Journal of Machine Learning Research, 17(1), 3537-3580.</li>
   </ul>
  </section>
    """,
}
