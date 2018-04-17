**University of California, Berkeley, Department of Physics**

**PHY151: Fall 2018**

Data science and Bayesian statistics for physical sciences
====================================================================

Instructor: Uro&#353; Seljak, Campbell Hall 359, useljak@berkeley.edu <br>
&nbsp; Office hours: Monday 12:30-1:30PM, Campbell 359 (knock on the glass door if you do not have access)

GSI: Byeonghee Yu, bhyu@berkeley.edu <br>
&nbsp; Office hours: Friday 2-3PM, Location TBD

Lecture: Monday, Wednesday 11AM-12:30AM, 251 LeConte Hall <br>
Discussion: Thursday, 1-2PM, Location TBD



Class Number: 46359

Course Syllabus
---------------

**Learning goals**:
The goals of the course is to get acquainted with modern computational methods
used in physical sciences, including numerical analysis methods, data science and Bayesian statistics. 
We will introduce a number of concepts that are useful in physical sciences at varying depth levels. We will cover main numerical methods used in physical sciences. Most of the statistical concepts will be Bayesian, 
emphasizing the concepts that have a connection to physical sciences, such as classical and statistical mechanics. We will focus on data science and data analysis applications that are often encountered in real world of physical sciences. Moreover, we will review many of the machine learning concepts and methods. 

**Target audience**:
target student population are upper division undergraduates from physical science departments, as well as beginning graduate students from the same departments. The course is also suitable for graduate students looking for an introduction to programming and numerical 
methods in phython.

**Course structure**:
each week there will be a set of 3 hour lectures discussing theoretical and practical underpinnings of the specific topic,
together with its most common applications in physical sciences. Class participation is expected in the form of weekly reading the lecture in advance, submitting comments and questions on the lecture and answering a short set of questions. There will be eight python based homework assignments, applying the methods to physical science based applications. A weekly one hour discussion will focus on the lecture material and homeworks. There will be 3 longer projects spread over the term.

**Prerequsites**:
Undergraduate students: PHY7 or PHY5 series, basic introduction to Python programming at the level of PHY77 or permission from instructor. Some knowledge of analytic mechanics and statistical physics at the level of PHY105 and PHY112 will be assumed. Graduate students: none. 

**Grades**: 30% projects, 40% homeworks, 30% class participation. Taking the course for Pass/Fail requires 50% of the work completed. 

Weekly Syllabus
---------------
**Numerical integration**: from Simpson to Romberg, proper and improper integrals, Gaussian quadratures, multi-dimensional integrals

References: Chapter 4 of Numerical Recipes (NR) & Chapter 5 of Newman, Computational Physics

**Introduction to probability and Bayesian inference**: general rules of probability, generating functions, moments and cumulants, binomial and multinomial, Poisson, gaussian distributions, multi-variate distributions, joint probability, marginal probability, Bayes theorem, forward and inverse probability, from probability to inference and the meaning of probability, prior, likelihood and posterior, interval estimates, comparison between Bayesian and classical statistics, Bayesian versus classical hypothesis testing (p-value) 

References: Ch. 2.1-2.3, 3 of MacKay, Ch. 2 of Kardar, Ch. 1-2 of Gelman et al, Bayesian data analysis

**More on Bayesian inference and intro to data modeling**: informative and noninformative priors, maximum a posteriori (MAP) and maximum likelihood estimator (MLE), asymptotic theorems, least square as MAP/MLE, fitting data to a straight line and a general linear least square model, normal equations

Reference: Ch. 15 of NR, Ch. 3, 4 of Gelman et al. 

**Linear Algebra**: gaussian and Gauss-Jacobi elimination, backsubstitution, pivoting, LU decomposition, Cholesky decomposition, QR decomposition,  sparse matrix linear algebra, solving linear equations with linear algebra, QR decomposition and tridiagonal forms, diagonalization of a symmetric and non-symmetric matrix, principal axes and covariance matrix, singular value decomposition (SVD), application to normal equations, principal component analysis (PCA) and dimensionality reduction, independent component analysis (ICA)

Reference: Ch. 2,11 of NR & Ch. 6 of Newman, https://arxiv.org/pdf/1404.2986.pdf

**Information theory**: Shannon information and mixing entropy, entropy for continuous variables and maximum entropy distributions, Kullback-Leibler divergence, negentropy, statistical independence, mutual and multi-information (application: FastICA), ensemble averaging: log likelihood as entropy,  curvature matrix (Hessian) as Fisher information matrix. Experiment design.  

Reference: Ch. 2 of MacKay, Ch. 2 of Kardar, https://arxiv.org/pdf/1404.2986.pdf

**Nonlinear equations and 1-d optimization**: bisection, Newton-Raphson, secant, false position method. Golden ratio, parabolic optimization. Relaxation methods. 

Reference: Newman Ch. 6, NR Ch. 9

**Optimization in many dimensions**: 1st order:gradient descent, stochastic gradient descent, mini-batch gradient descent. Momentum and Nesterov acceleration, ADAM. 2nd order methods: general strategies: choosing direction, doing line search or trust region. Newton, quasi-Newton, Gauss-Newton, conjugate gradient, Levenberg-Malmquardt method. 

Reference: Nocedal & Wright, Optimization. NR 9,10,15. 

**Monte Carlo methods for integration and posteriors**: Simple Monte Carlo. Random number generators: transform method, Box-Muller for gaussian, Cholesky for multivariate gaussians, rejection sampling. Importance sampling for posteriors and for integration. Markov Chain Monte Carlo: Metropolis and Metropolis-Hastings. Convergence tests: burn-in, Gelman-Rubin statistic and chain correlation length. Improving efficiency: proposal function, Gibbs sampler with conditional conjugate distributions. Simulated annealing and simulated tampering. Hamiltonian Monte Carlo. Other MCMC approaches. 

References: NR, Press etal., Ch.7, Newman, Ch. 10, Gelman et al. Ch 10-12, MacKay Ch. 20-22

**More advanced Bayesian analysis**: probabilistic graphical models, hierarchical Bayesian models, model checking and evaluation, dealing with outliers

References: Gelman et al. Ch. 5, 6, 7, 17

**Variational approximations**: conditional and marginal approximations, expectation maximization and gaussian mixture model, variational inference and variational Bayes, expectation propagation

References: Gelman Ch 13, 22

**Interpolation and extrapolation of data**: polynomial, rational and spline interpolation, gaussian processes for regression and for classification

References: NR Ch. 5, Gelman Ch. 21

**Fourier methods**: Fast Fourier transforms (FFT), FFT convolutions, power spectrum and correlation function, Wiener filtering and missing data, matched filtering, wavelets

References: NR Ch. 12, 13

**Ordinary and partial differential equations**: Euler, Runge Kutta, Bulirsch-Stoer, stiff equation solvers, leap-frog and symplectic integrators, Partial differential equations: boundary value and initial value problems

References: NR Ch. 17, 18, 20

**Classification and inference with machine learning**: supervised and unsupervised learning, naive Bayes, Decision Tree-Based methods, Support Vector Machines, KNN, random forest, neural networks, deep networks, adversarial networks, automated differentiation: back and forward propagation, inference: logistic function, ReLU

References: NR Ch. 16

Literature
----------

- [Numerical Recipes](http://numerical.recipes), by Press. W. et al.

- [Information Theory, Inference and Learning Algorithms](http://www.inference.phy.cam.ac.uk/mackay/itila/book.html), by David MacKay

- Bayesian data analysis, 3rd edition, by Gelman A., et al.

- [An Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/ISLR%20Sixth%20Printing.pdf), by James G. etal, 

- [A Survey of Computational Physics](http://www.compadre.org/psrc/items/detail.cfm?ID=11578) by Landau, R., Paez, M-J., Bordeianu, C.

- <http://greenteapress.com/wp/think-bayes/>

- <https://github.com/CamDavidsonPilon/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers>

- [Computational Physics](http://www-personal.umich.edu/~mejn/cp/chapters/int.pdf) by Mark Newman

- Effective Computation in Physics, by A. Scopatz and K. D. Huff

- [From Python to Numpy](https://www.labri.fr/perso/nrougier/from-python-to-numpy/) by N. P. Rougier

[//]: # (THESE WERE COMMENTED OUT )

[//]: # (opinionated lectures in statistics by Press W., )

[//]: # (http://wpressutexas.net/coursewiki/index.php/OpinionatedLessons.org/ )

[//]: # (mathematicalmonk series of videos by Jeff Miller, https://www.youtube.com/user/mathematicalmonk/playlists?spfreload=10 )

[//]: # (Various other resources )

[//]: # (https://arxiv.org/pdf/1505.02965.pdf)

[//]: # (https://arxiv.org/abs/1701.02434)

Other resources will be provided according to the needs.

Software
--------

We will use Python Jupyter hub environment. You are expected to use existing numerical analysis routines and not write your own. Most of these are already
implemented in python libraries (scipy, numpy...).

[//]: # (Routines that go with Landau's book are at)
[//]: # (http://www.science.oregonstate.edu/~landaur/Books/CPbook/Codes/PythonCodes/)

Homeworks and Projects
------------------------

Throughout the course, students will complete and electronically submit one homework assignment (code) per week.
This code will be run on test cases to check if it produces appropriate results. Students are encouraged to discuss 
homeworks with other students, but should submit their own solutions. Homeworks will use the concepts developed in the 
lectures and apply to relatively simple problems. 

Projects are larger assignments intended to teach you how to combine ideas from the course in interesting ways and apply them 
to real data. There are three projects during the semester. You are encouraged to complete projects in pairs; your partner should be another student in your section. Work together to ensure that both group members understand the complete program you create.

Homeworks and projects are to be submitted using Jupyter notebook in Python.

Sample projects: 

1) **Planck satellite data analysis**: use measurement of Planck satellite power spectrum to determine cosmological parameters. First use linear algebra to solve the least square problem and find MAP/MLE best fit parameters. Next use optimization to solve for the same. Determine covariances of all parameters using Laplace approximation. Make predictions for future experiments with lower noise using Fisher matrix experiment design predictions. Use Planck published MCMC chains and analyze their burn-in phase, Gelman-Rubin statistics, and chain correlations. Plot their 1-d and 2-d distributions and compare them to MAP/Laplace approximation. Change one parameter and use importance sampling to produce new posteriors.  

2) **LIGO Nobel prize data analysis**: use matched filtering methods and FFT to analyze first LIGO event and show it has detected gravitational waves.

3) **Machine learning on galaxies**: use SDSS galaxy flux photometric measurements and redshift measurements to train the ML algorithms for regression, determining the redshift. Use verification data to test the training algorithms. Try KNN, gaussian processes, linear and quadratic regression, support vector machines, neural networks, random forest... Next try classification: use galaxy zoo galaxy morphology (spirals ellipticals, irregulars...) training data and apply to SDSS. Use photometry first, then add image information and observe how the accuracy improves. 
