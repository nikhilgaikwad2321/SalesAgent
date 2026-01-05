package com.crm.ai.controller;

import lombok.extern.slf4j.Slf4j;
import org.springframework.core.io.Resource;
import org.springframework.core.io.UrlResource;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

import java.net.MalformedURLException;
import java.nio.file.Path;
import java.nio.file.Paths;

@RestController
@RequestMapping("/api/ppt")
@Slf4j
public class PptDownloadController {

    private static final String LLM_RUNTIME_BASE_URL = "http://localhost:8000";

    @GetMapping("/download/{filename}")
    public ResponseEntity<byte[]> downloadPpt(@PathVariable String filename) {
        try {
            log.info("Downloading PPT file: {}", filename);
            
            // Proxy request to LLM Runtime service
            RestTemplate restTemplate = new RestTemplate();
            String url = LLM_RUNTIME_BASE_URL + "/api/llm/ppt/download/" + filename;
            
            ResponseEntity<byte[]> response = restTemplate.getForEntity(url, byte[].class);
            
            return ResponseEntity.ok()
                    .contentType(MediaType.parseMediaType("application/vnd.openxmlformats-officedocument.presentationml.presentation"))
                    .header(HttpHeaders.CONTENT_DISPOSITION, "attachment; filename=\"" + filename + "\"")
                    .body(response.getBody());
                    
        } catch (Exception e) {
            log.error("Error downloading PPT file: {}", filename, e);
            return ResponseEntity.notFound().build();
        }
    }
}
