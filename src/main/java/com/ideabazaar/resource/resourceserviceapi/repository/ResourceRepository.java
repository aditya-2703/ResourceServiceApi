package com.ideabazaar.resource.resourceserviceapi.repository;

import com.ideabazaar.resource.resourceserviceapi.model.Resource;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public  interface ResourceRepository extends JpaRepository<Resource, Long> {
    List<Resource> findResourceByProjectId(Long id);
}
